#!/usr/bin/env python3
"""
Sync ng_lesson notebooks from DeepLearning.AI.

Requires an authenticated session cookie for notebook access.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
import socket
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse, urlunparse, quote
from urllib.request import Request, urlopen

TRPC_BASE = "https://learn.deeplearning.ai/api/trpc"
COURSE_SLUG = "ai-python-for-beginners"
ALLOWED_TYPES = {"video_notebook", "notebook"}

IGNORE_DIRS = {".ipynb_checkpoints", "__pycache__", ".git"}
COOKIE_KEYS = ("DLAI_SESSION_COOKIE", "DLAI_COOKIE")
LESSON_ALIASES = {
    "running your first program": "Lesson 4 - Running your first program",
    "data in python": "Lesson 6 - Data in Python",
    "combining text and calculations": "Lesson 7 - Combining text and calculations",
    "variables": "Lesson 8 - Variables",
    "building llm prompts with variables": "Lesson 9 - Building LLM prompts with variables",
    "functions actions on data": "Lesson 10 - Functions - Actions on Data",
    "next course preview working with files": "Lesson 7 - Next course preview - working with files",
}


def http_get(url: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> str:
    if params:
        url = f"{url}?{urlencode(params)}"
    final_headers = {
        "Accept": "application/json",
        "Accept-Encoding": "identity",
        "User-Agent": "ng-lesson-sync/1.0",
    }
    if headers:
        final_headers.update(headers)
    req = Request(url, headers=final_headers)
    for attempt in range(1, 6):
        try:
            with urlopen(req, timeout=60) as resp:
                return resp.read().decode("utf-8")
        except HTTPError as exc:
            body = exc.read().decode("utf-8") if exc.fp else ""
            if exc.code in {502, 503, 504} and attempt < 5:
                time.sleep(5 * attempt)
                continue
            raise RuntimeError(f"HTTP {exc.code} for {url}: {body}") from exc
        except (TimeoutError, socket.timeout) as exc:
            if attempt < 5:
                time.sleep(5 * attempt)
                continue
            raise RuntimeError(f"Network timeout for {url}: {exc}") from exc
        except URLError as exc:
            if attempt < 5:
                time.sleep(5 * attempt)
                continue
            raise RuntimeError(f"Network error for {url}: {exc}") from exc
    raise RuntimeError(f"Failed to fetch {url} after retries")


def trpc_query(procedure: str, payload: Dict[str, Any], cookie: Optional[str]) -> Dict[str, Any]:
    url = f"{TRPC_BASE}/{procedure}"
    params = {"input": json.dumps({"json": payload})}
    headers = {"Cookie": cookie} if cookie else {}
    raw = http_get(url, params=params, headers=headers)
    data = json.loads(raw)
    if "error" in data:
        message = data["error"].get("json", {}).get("message", data["error"])
        raise RuntimeError(f"tRPC {procedure} error: {message}")
    return data["result"]["data"]["json"]


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    return cleaned.strip("-")


def lesson_url(course_slug: str, lesson_slug: str, lesson_name: str) -> str:
    return f"https://learn.deeplearning.ai/courses/{course_slug}/lesson/{lesson_slug}/{slugify(lesson_name)}"


def parse_env_file(env_path: Path) -> Dict[str, str]:
    if not env_path.exists():
        return {}
    env_vars: Dict[str, str] = {}
    for line in env_path.read_text(encoding="utf-8").splitlines():
        raw = line.strip()
        if not raw or raw.startswith("#"):
            continue
        if raw.startswith("export "):
            raw = raw[len("export ") :].strip()
        if "=" not in raw:
            continue
        key, value = raw.split("=", 1)
        key = key.strip()
        value = value.strip().strip("\"'")  # keep it simple; cookie has no quotes
        if key:
            env_vars[key] = value
    return env_vars


def load_cookie(args: argparse.Namespace) -> Optional[str]:
    if args.cookie:
        return args.cookie.strip()
    if args.cookie_file:
        return Path(args.cookie_file).read_text(encoding="utf-8").strip()
    for key in COOKIE_KEYS:
        env_value = os.getenv(key)
        if env_value:
            return env_value.strip()
    env_path = Path(__file__).resolve().parents[1] / ".env"
    env_vars = parse_env_file(env_path)
    for key in COOKIE_KEYS:
        value = env_vars.get(key)
        if value:
            return value.strip()
    return None


def normalize_cookie(cookie: Optional[str]) -> Optional[str]:
    if not cookie:
        return None
    raw = cookie.strip()
    if "next-auth.session-token" not in raw and "__Secure-next-auth.session-token" not in raw:
        if raw.count(".") >= 2 and "=" not in raw:
            raw = f"next-auth.session-token={raw}"
        return raw
    pairs = [p.strip() for p in raw.split(";") if p.strip()]
    token_value = None
    has_next = False
    has_secure = False
    for pair in pairs:
        if pair.startswith("next-auth.session-token="):
            has_next = True
            token_value = pair.split("=", 1)[1].strip()
        elif pair.startswith("__Secure-next-auth.session-token="):
            has_secure = True
            token_value = pair.split("=", 1)[1].strip()
    if token_value and not has_secure:
        pairs.append(f"__Secure-next-auth.session-token={token_value}")
    if token_value and not has_next:
        pairs.append(f"next-auth.session-token={token_value}")
    return "; ".join(pairs)


def find_existing_lesson_dir(module_dir: Path, lesson_name: str) -> Optional[Path]:
    if not module_dir.exists():
        return None
    normalized = re.sub(r"[^a-z0-9]+", " ", lesson_name.lower()).strip()
    alias = LESSON_ALIASES.get(normalized)
    if alias:
        alias_path = module_dir / alias
        if alias_path.exists():
            return alias_path
    for child in module_dir.iterdir():
        if not child.is_dir():
            continue
        name = child.name
        name = re.sub(r"^(lesson\\s*\\d+\\s*-\\s*|l\\s*\\d+\\s*-\\s*)", "", name, flags=re.I)
        candidate = re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()
        if candidate == normalized:
            return child
    return None


def find_existing_module_dir(output_root: Path, module_label: str) -> Optional[Path]:
    if not output_root.exists():
        return None
    prefix = f"{module_label} "
    matches = [child for child in output_root.iterdir() if child.is_dir() and child.name.startswith(prefix)]
    if len(matches) == 1:
        return matches[0]
    return None


def infer_api_base(lab_url: str) -> Tuple[str, Optional[str]]:
    parsed = urlparse(lab_url)
    token = None
    if parsed.query:
        for part in parsed.query.split("&"):
            if part.startswith("token="):
                token = part.split("=", 1)[1]
                break
    path = parsed.path or ""
    for marker in ("/lab", "/notebooks", "/tree"):
        if marker in path:
            path = path.split(marker)[0]
            break
    base = urlunparse((parsed.scheme, parsed.netloc, path.rstrip("/"), "", "", ""))
    api_base = f"{base}/api/contents"
    return api_base, token


def api_contents(api_base: str, path: str, token: Optional[str], cookie: Optional[str]) -> Dict[str, Any]:
    encoded_path = quote(path, safe="/") if path else ""
    url = f"{api_base}/{encoded_path}" if encoded_path else api_base
    params: Dict[str, Any] = {"content": 1}
    if token:
        params["token"] = token
    headers = {"Cookie": cookie} if cookie else {}
    raw = http_get(url, params=params, headers=headers)
    return json.loads(raw)


def api_download(
    api_base: str,
    path: str,
    token: Optional[str],
    cookie: Optional[str],
    fmt: Optional[str] = None,
) -> Dict[str, Any]:
    encoded_path = quote(path, safe="/") if path else ""
    url = f"{api_base}/{encoded_path}" if encoded_path else api_base
    params: Dict[str, Any] = {"content": 1}
    if fmt:
        params["format"] = fmt
    if token:
        params["token"] = token
    headers = {"Cookie": cookie} if cookie else {}
    raw = http_get(url, params=params, headers=headers)
    return json.loads(raw)


def find_notebooks(api_base: str, token: Optional[str], cookie: Optional[str]) -> List[str]:
    notebooks: List[str] = []
    stack = [""]
    while stack:
        current = stack.pop()
        listing = api_contents(api_base, current, token, cookie)
        if listing.get("type") != "directory":
            continue
        for item in listing.get("content", []):
            name = item.get("name", "")
            item_type = item.get("type")
            item_path = item.get("path", "")
            if item_type == "directory":
                if name in IGNORE_DIRS:
                    continue
                stack.append(item_path)
            elif item_type == "notebook" or name.endswith(".ipynb"):
                notebooks.append(item_path)
    return notebooks


def pick_notebook(notebooks: List[str], lesson_name: str) -> Optional[str]:
    if not notebooks:
        return None
    if len(notebooks) == 1:
        return notebooks[0]
    needle = re.sub(r"[^a-z0-9]", "", lesson_name.lower())
    for path in notebooks:
        base = re.sub(r"[^a-z0-9]", "", Path(path).stem.lower())
        if needle and needle in base:
            return path
    return notebooks[0]


def write_notebook(dest: Path, notebook: Dict[str, Any]) -> None:
    dest.write_text(json.dumps(notebook, ensure_ascii=False, indent=2), encoding="utf-8")


def notebook_to_markdown(nb: Dict[str, Any]) -> str:
    chunks: List[str] = []
    for cell in nb.get("cells", []):
        cell_type = cell.get("cell_type")
        source = "".join(cell.get("source", [])).rstrip()
        if not source:
            continue
        if cell_type == "markdown":
            chunks.append(source)
        elif cell_type == "code":
            chunks.append(f"```python\n{source}\n```")
        elif cell_type == "raw":
            chunks.append(source)
    return "\n\n".join(chunks).rstrip() + "\n"


def download_tree(
    api_base: str,
    root_path: str,
    dest_root: Path,
    token: Optional[str],
    cookie: Optional[str],
    skip_paths: Iterable[str],
) -> None:
    skip_set = set(skip_paths)
    listing = api_contents(api_base, root_path, token, cookie)
    if listing.get("type") != "directory":
        return
    for item in listing.get("content", []):
        name = item.get("name", "")
        item_type = item.get("type")
        item_path = item.get("path", "")
        if item_path in skip_set:
            continue
        if item_type == "directory":
            if name in IGNORE_DIRS:
                continue
            target_dir = dest_root / name
            target_dir.mkdir(parents=True, exist_ok=True)
            download_tree(api_base, item_path, target_dir, token, cookie, skip_paths)
            continue
        if item_type == "notebook" or name.endswith(".ipynb"):
            continue
        target_file = dest_root / name
        payload = api_download(api_base, item_path, token, cookie)
        if payload.get("type") == "file":
            content = payload.get("content", "")
            if payload.get("format") == "base64":
                target_file.write_bytes(base64.b64decode(content))
            else:
                target_file.write_text(content, encoding="utf-8")


def sync_lesson(
    course_id: int,
    program_id: int,
    lesson_name: str,
    dest_dir: Path,
    cookie: Optional[str],
) -> None:
    lab = None
    for attempt in range(1, 13):
        try:
            lab = trpc_query(
                "course.getProgramLab",
                {"programAssignmentId": program_id, "courseId": course_id, "userId": -1},
                cookie,
            )
            break
        except RuntimeError as exc:
            message = str(exc)
            if "Sandbox" in message and attempt < 12:
                print(f"Lab is launching, retrying in 10s (attempt {attempt}/12)")
                time.sleep(10)
                continue
            raise
    if not lab:
        raise RuntimeError("Failed to obtain program lab after retries")
    lab_url = lab.get("url")
    if not lab_url:
        raise RuntimeError("Program lab response missing url")
    api_base, token = infer_api_base(lab_url)
    notebooks = find_notebooks(api_base, token, cookie)
    notebook_path = pick_notebook(notebooks, lesson_name)
    if not notebook_path:
        raise RuntimeError("No notebook found in lab environment")

    notebook_payload = api_download(api_base, notebook_path, token, cookie)
    content = notebook_payload.get("content")
    if isinstance(content, str):
        notebook = json.loads(content)
    else:
        notebook = content

    dest_dir.mkdir(parents=True, exist_ok=True)
    base_name = dest_dir.name
    ipynb_path = dest_dir / f"{base_name}.ipynb"
    md_path = dest_dir / f"{base_name}.md"

    write_notebook(ipynb_path, notebook)
    md_path.write_text(notebook_to_markdown(notebook), encoding="utf-8")

    parent_path = str(Path(notebook_path).parent).lstrip(".")
    download_tree(api_base, parent_path, dest_dir, token, cookie, skip_paths=[notebook_path])


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync ng_lesson notebooks from DeepLearning.AI")
    parser.add_argument("--course-slug", default=COURSE_SLUG)
    parser.add_argument("--output-root", default="references/ng_lesson")
    parser.add_argument("--cookie", help="Session cookie string, e.g. next-auth.session-token=...")
    parser.add_argument("--cookie-file", help="Path to file containing session cookie")
    parser.add_argument("--list-only", action="store_true", help="List lesson URLs without syncing")
    parser.add_argument(
        "--module-label",
        action="append",
        help="Limit sync to a module label, e.g. 'Module 1' (repeatable)",
    )
    parser.add_argument(
        "--lesson-name",
        action="append",
        help="Limit sync to a lesson name (repeatable, exact match)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=3,
        help="Process lessons in batches of N with pauses (0 to disable).",
    )
    parser.add_argument(
        "--batch-pause",
        type=int,
        default=15,
        help="Seconds to pause between batches when batch-size > 0.",
    )
    args = parser.parse_args()

    cookie = normalize_cookie(load_cookie(args))
    course = trpc_query("course.getCourseBySlug", {"courseSlug": args.course_slug}, None)
    course_id = course.get("courseId")
    lessons = course.get("lessons", {})
    listing = course.get("listing", [])

    output_root = Path(args.output_root)
    if not listing:
        print("No modules found in course listing.")
        return 1

    allowed_modules = set(args.module_label or [])
    allowed_lessons = set(args.lesson_name or [])
    batch_size = max(0, args.batch_size)
    batch_pause = max(0, args.batch_pause)
    processed_in_batch = 0

    for module in listing:
        module_label = module.get("moduleLabel", "Module")
        module_name = module.get("name", "")
        if allowed_modules and module_label not in allowed_modules:
            continue
        module_dir = output_root / f"{module_label} {module_name}".strip()
        existing_module_dir = find_existing_module_dir(output_root, module_label)
        if existing_module_dir:
            module_dir = existing_module_dir
        content = module.get("content", [])
        video_idx = 0

        for item in content:
            key = item.get("key")
            lesson = lessons.get(key, {})
            lesson_type = lesson.get("type")
            lesson_name = lesson.get("name")
            lesson_slug = lesson.get("slug")
            program_id = lesson.get("programId")

            if lesson_type == "video_notebook":
                video_idx += 1
            if allowed_lessons and lesson_name not in allowed_lessons:
                continue
            if lesson_type not in ALLOWED_TYPES:
                continue

            if not lesson_name or not lesson_slug:
                continue

            url = lesson_url(args.course_slug, lesson_slug, lesson_name)
            if args.list_only:
                print(f"{module_label} | {lesson_name} | {lesson_type} | {url}")
                continue

            if not cookie:
                raise RuntimeError("Missing session cookie. Set --cookie/--cookie-file or DLAI_SESSION_COOKIE.")
            if not program_id:
                print(f"Skip {lesson_name}: missing programId")
                continue

            existing_dir = find_existing_lesson_dir(module_dir, lesson_name)
            if existing_dir:
                dest_dir = existing_dir
            else:
                if lesson_type == "notebook" and "install python" in lesson_name.lower():
                    folder_name = lesson_name
                else:
                    folder_name = f"Lesson {video_idx} - {lesson_name}"
                dest_dir = module_dir / folder_name

            print(f"Syncing {lesson_name} -> {dest_dir}")
            sync_lesson(course_id, program_id, lesson_name, dest_dir, cookie)
            if not args.list_only and batch_size:
                processed_in_batch += 1
                if processed_in_batch >= batch_size:
                    if batch_pause:
                        print(f"Batch complete. Pausing {batch_pause}s to reduce timeouts.")
                        time.sleep(batch_pause)
                    processed_in_batch = 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
