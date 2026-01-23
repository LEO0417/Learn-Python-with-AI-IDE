---
description: Run a continuity check on a lesson file to ensure titles and flow are consistent.
---

Usage: `/check-continuity <lesson-path-basename>` (e.g., `M1L7`)

Steps:
1.  **Baseline Check**: Identify the SC (`.md`) and TC (`_TW.md`) versions of the lesson.
2.  **Context Loading**: Read the conclusion of the previous lesson (L-1) and the introduction of the next lesson (L+1, if exists) to check transition consistency.
3.  **Terminology Alignment**: Use `lesson-ops` (Continuity Check section) and `chinese-terminology-checker` to ensure SC uses Mainland China terms and TC uses Taiwan terms.
4.  **Logic & Flow Polish**: Check for redundancy with L-1 or missing links to L+1. Ensure "AI as files" and other core metaphors are consistent.
5.  **Title Verification**: Match titles in file headers, intro/outro text, and `docs/PROJECT_STATE.md`.
6.  **Title Snapshot**: Update `docs/PROJECT_STATE.md` if the current lesson is finalized, ensuring the SC/TC/EN titles are correctly reflected in the uniform format.
7.  **Correction**: Execute `multi_replace_file_content` to fix all identified issues.
