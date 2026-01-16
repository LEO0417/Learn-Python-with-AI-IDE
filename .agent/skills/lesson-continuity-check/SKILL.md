---
name: lesson-continuity-check
description: Check lesson continuity (titles, flow, references) after content creation. Adheres to Section 4 (Content Locking) of lesson-authoring-guide.
---

# Lesson Continuity Check (课程连贯性检查)

Whenever you finish editing or creating a lesson file (e.g., `M1L3.md`), you MUST perform this check to ensure seamless reading flow.

## 1. Title Consistency (标题一致性)
- **Check**: Does the lesson title in the file header (`# Module X Lesson Y: Title`) match:
    - The actual filename?
    - The title referenced in the **Previous Lesson's Conclusion (Next Lesson Preview)**?
    - The title referenced in the **Next Lesson's Introduction (Previous Lesson Recap)**?
    - The `docs/MAPPING.md` mapping table?
    - The relevant task tracker (`docs/MODULE_1_TASKS.md` or `docs/MODULE_2_TASKS.md`)?
- **Action**: If there is a mismatch, update **ALL** occurrences to the single source of truth.

## 2. Intro/Outro Flow (首尾呼应)
- **Introduction (Opening)**:
    - Does it explicitly mention the **Previous Lesson** by name/concept?
    - Does it explain *why* we are here based on *where* we came from? (e.g., "Now that we have installed Python (L3), let's protect it (L4).")
- **Conclusion (Closing)**:
    - Does it explicitly name the **Next Lesson**?
    - Does it provide a "Cliffhanger" or logical bridge? (e.g., "But how do we save this code? Find out in [Next Lesson Title].")
    - **CRITICAL**: The "Next Lesson Title" used here MUST match the actual title of the next file.

## 3. Terminology Synchrony (术语一致性)
- **Concept Mapping**: Ensure terms match `chinese-terminology-checker/GLOSSARY.md`.
- **SC Tone**: Use Mainland China terms (e.g., 资源管理器, 终端, 文件夹, 项目).
- **TC Tone**: Use Taiwan terms (e.g., 檔案總管, 終端機, 資料夾, 專案).
- **Global Consist**: If a specific metaphor is used (e.g., "AI Ready Engineer"), ensure it's consistently translated and used across all modules.

## 4. Logic & Flow Consistency (逻辑与讲述一致性)
- **Difficulty Curve**: Ensure L7 doesn't repeat what was completely covered in L6, or skip a necessary prerequisite.
- **Narrative Persona**: Ensure the "Voice" remains consistent (Professional, Rigorous & Welcoming).
- **Concept Chain**: If L7 introduces "AI brain as files", does it conflict with L1-L6's mental model? (It should supplement, not contradict).

## 5. Verification Workflow
1.  **Read Target**: Read the target lesson (SC and TC).
2.  **Read Context**: Read the previous lesson (L-1 conclusion) and the next lesson (L+1 intro).
3.  **Cross-Check Titles**: Verify all titles match across file, intro, outro, and `MAPPING.md`.
4.  **Polish & Align**: Apply corrections to terminology and logic transitions.
