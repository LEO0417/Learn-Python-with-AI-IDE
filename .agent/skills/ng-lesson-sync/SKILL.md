---
name: ng-lesson-sync
description: Sync DeepLearning.AI "ai-python-for-beginners" course materials into references/ng_lesson using the bundled sync script. Use when asked to refresh ng_lesson, update official course snapshots, or run the ng_lesson sync workflow.
---

# Ng Lesson Sync

## Overview
Use the bundled script (`.agent/skills/ng-lesson-sync/scripts/ng_lesson_sync.py`) to pull official ng_lesson notebooks, helper files, and assets into `references/ng_lesson/`.

## Workflow
1) Confirm scope (modules and/or lessons) and that this is an official update.
2) Ensure the login cookie is stored in `.env` and not committed (see `.gitignore`).
3) Preview the official lesson URLs:
   - `python .agent/skills/ng-lesson-sync/scripts/ng_lesson_sync.py --list-only`
4) Sync with filters and batching if needed:
   - `python .agent/skills/ng-lesson-sync/scripts/ng_lesson_sync.py --module-label "Module 2"`
   - `python .agent/skills/ng-lesson-sync/scripts/ng_lesson_sync.py --lesson-name "Lesson Name"`
   - Adjust batching with `--batch-size` and `--batch-pause`.
5) Record the sync in `docs/WORKLOG/YYYY-MM-DD.md` with scope and source URL.

## Notes
- Do not modify `references/` unless it is an official update.
- Keep credentials in `.env`; never commit them.
- The script is stored in `.agent/skills/ng-lesson-sync/scripts/ng_lesson_sync.py`.
