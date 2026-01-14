---
description: Perform a safe git commit with bilingual messages and pre-flight checks.
---

Usage: `/git`

Steps:
1. **Audit**: Run `git status` and analyze the current session's key decisions.
2. **Worklog Sync**: Automatically update `docs/WORKLOG/YYYY-MM-DD.md` with a summary of technical and curriculum changes.
3. **Safety Scan**: Verify the blocklist (e.g., `.env`, `.DS_Store`).
4. **Daily Node Choice**: 
    - If a commit for Today exists: Propose **Amending** with updated details.
    - If not: Propose a **New Commit**.
5. **Execution**: Perform the Git operation after user confirmation.
