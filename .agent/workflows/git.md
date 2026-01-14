---
description: Perform a safe git commit with bilingual messages and pre-flight checks.
---

Usage: `/git`

Steps:
1. **Safety Scan**: Run `git status` to identify all staged and unstaged changes.
2. **Skill Check**: Use the `git-collaboration` skill to verify if any sensitive or redundant files (like `.env` or `.DS_Store`) are accidentally included.
3. **Bilingual Message**: Generate a commit message based on the recent changes in both English and Chinese.
4. **User Confirmation**: Present the summary of changes and the proposed commit message.
5. **Execution**: Execute `git add .` and `git commit -m "..."` only after receiving final confirmation.
