---
name: lesson-ops
description: A unified skill for curriculum development operations, including scaffolding new lessons (/sl) and checking continuity (/cc).
---

# Lesson Operations (课程开发套件)

This skill consolidates the workflow for creating (scaffolding) and verifying (continuity check) curriculum content.

## 1. Scaffold Lesson (`/sl`)
**Goal**: Build a standard 7-stage lesson skeleton.

### Workflow
1.  **Clarify Scope**:
    *   Read `docs/PROJECT_STATE.md` to identify the module context and "Next Lesson" requirements.
    *   Read `docs/MAPPING.md` (if exists) or the Mapping section in PROJECT_STATE.
2.  **Generate Skeleton**:
    *   Use the standard template defined in `lesson-authoring-guide`.
    *   **Snippet**:
        ```markdown
        # Module X Lesson Y: [Title]
        > **课程体系：Learn Python with AI IDE** ...
        ---
        ## 1. 🔙 Backtrack ...
        ```
3.  **Quality Check**:
    *   Ensure tone is "Professional" (No juvenile metaphors).
    *   Use correct SC/TC terminology.

## 2. Continuity Check (`/cc`)
**Goal**: Ensure seamless flow and consistency between lessons.

### Workflow
1.  **Title Verification**:
    *   Check if `# Title` matches `docs/PROJECT_STATE.md`.
    *   Check if "Next Lesson" in L-1 matches L.
    *   Check if "Previous Lesson" in L matches L-1.
2.  **Flow Logic**:
    *   **Intro**: Does it explicitly bridge from the previous skill?
    *   **Outro**: Does it set a cliffhanger for the next file?
3.  **Terminology**:
    *   Verify against `chinese-terminology-checker`.
4.  **Auto-Correction**:
    *   If titles mismatch, update `PROJECT_STATE.md` (if L is final) or the Lesson file.

## 3. Reference
*   **Standards**: `.agent/skills/lesson-authoring-guide/SKILL.md`
*   **Source of Truth**: `docs/PROJECT_STATE.md`
