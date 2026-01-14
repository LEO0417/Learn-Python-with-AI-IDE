---
name: git-collaboration
description: Standards for Git operations, including bilingual commit messages and safety checks for sensitive or redundant files.
---

# Git Collaboration Standards

## 1. Commit Message Convention
Every commit MUST have a bilingual message (English & Chinese) following this format:
`[Category] Action description | 动作描述`

Categories:
- `feat`: New lesson or feature.
- `fix`: Correction of content or logic.
- `docs`: Documentation updates.
- `refactor`: Restructuring files or content without changing the "meaning".
- `chore`: Maintenance (e.g., updating skills/workflows).

Example:
`feat: Complete M1L7 standard workbench TW | 完成 M1L7 标准工作台繁体版`

## 2. Pre-commit Safety Check
Before committing, the Agent must scan the staged files for:
- **Sensitive Data**: `.env`, credentials, or private keys.
- **OS Garbage**: `.DS_Store`, `Thumbs.db`.
- **Large/Redundant Binaries**: Large videos or loose images outside the `RESOURCES` folder.
- **WIP Files**: Files ending in `_WIP.md` or temporary scratchpads.

## 3. Workflow Logic (Implicit)
1.  Analyze `git status`.
2.  Compare against the "Blocked List".
3.  If a blocked file is found, **HALT** and warn the user.
4.  If safe, generate the bilingual message and propose the command.
