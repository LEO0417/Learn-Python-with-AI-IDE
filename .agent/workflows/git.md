---
description: Create a NEW git commit node explicitly, bypassing the daily-amend logic.
---

Usage: `/git`

Steps:
1. **Audit**: Run `git status` and analyze the current session's key decisions.
2. **Worklog Sync**: Automatically update `docs/WORKLOG/YYYY-MM-DD.md` with a summary.
3. **Safety Scan**: Verify the blocklist (e.g., `.env`, `.DS_Store`).
4. **Force New Node**: 
    - Explicitly create a **New Commit** object.
    - Do NOT use `--amend` even if a commit for today exists.
5. **Execution**: Perform the Git operation after user confirmation.
