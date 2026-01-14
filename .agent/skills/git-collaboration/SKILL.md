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

## 2. Commit Strategy: Daily Milestone & Worklog Sync
- **Goal**: Maintain a clean "one commit per day" history synced with professional worklogs.
- **Pre-flight Requirement**: 
    1. Before committing/amending, the Agent MUST analyze today's changes and conversation items.
    2. Sync these findings into the daily worklog file (e.g., `docs/WORKLOG/YYYY-MM-DD.md`).
- **Logic**:
    1. Check if `HEAD Date == Today` -> `git commit --amend`.
    2. Else -> Create new commit node.
- **Message Enrichment**: Integrate session updates into the existing commit's `Details` section.

## 3. Pre-commit Safety Check
Before committing, the Agent must scan the staged files for:
- **Sensitive Data**: `.env`, credentials, or private keys.
- **OS Garbage**: `.DS_Store`, `Thumbs.db`.
- **Large/Redundant Binaries**: Large videos or loose images outside the `RESOURCES` folder.
- **WIP Files**: Files ending in `_WIP.md` or temporary scratchpads.

## 4. Workflow Logic (Implicit)
1.  Analyze `git status` and conversation history.
2.  **Worklog Sync**: Update or create `docs/WORKLOG/YYYY-MM-DD.md` based on analyzed changes.
3.  Compare against the "Blocked List" for safety.
4.  Check `HEAD` commit date for Amend/Commit decision.
5.  Generate bilingual message and execute after confirmation.
