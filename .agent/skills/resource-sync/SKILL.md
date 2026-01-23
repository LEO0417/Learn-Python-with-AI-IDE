---
name: resource-sync
description: Unified skill for syncing external educational resources (DeepLearning.AI and Stanford CS146S) into local references.
---

# Resource Sync (外部资源同步)

## 1. DeepLearning.AI Sync (Ng Lesson)
**Target**: `references/ng_lesson/`
**Script**: `.agent/scripts/ng_lesson_sync.py`

### Workflow
1.  **Preparation**: Ensure cookies defined in `.env`.
2.  **Preview**: `python .agent/scripts/ng_lesson_sync.py --list-only`
3.  **Execute**:
    *   `python .agent/scripts/ng_lesson_sync.py --module-label "Module X"`
4.  **Log**: Update `docs/WORKLOG/`.

## 2. Stanford Office Code Sync (CS146S)
**Target**: `references/office-code/`
**Source**: `https://github.com/mihail911/modern-software-dev-assignments`

### Workflow
1.  **Clone/Fetch**: Use a temp directory (`/tmp/office-code-upstream`).
2.  **Diff**: Compare `/tmp/...` with local `references/office-code/`.
3.  **Sync**: `rsync -a` or `cp -R` content.
4.  **Safety**: Never overwrite local customizations without backup.
5.  **Log**: Record the official commit hash in `docs/WORKLOG/`.

## 3. General Rules
*   **Read-Only**: Treat `references/` as read-only snapshots.
*   **Traceability**: All sync actions must be logged.
