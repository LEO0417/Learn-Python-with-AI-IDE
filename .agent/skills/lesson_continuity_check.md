---
description: Check lesson continuity (titles, flow, references) after content creation.
---

# Lesson Continuity Check (课程连贯性检查)

Whenever you finish editing or creating a lesson file (e.g., `M1L3.md`), you MUST perform this check to ensure seamless reading flow.

## 1. Title Consistency (标题一致性)
- **Check**: Does the lesson title in the file header (`# Module X Lesson Y: Title`) match:
    - The actual filename?
    - The title referenced in the **Previous Lesson's Conclusion (Next Lesson Preview)**?
    - The title referenced in the **Next Lesson's Introduction (Previous Lesson Recap)**?
    - The `docs/MAPPING.md` or `docs/MODULE_1_TASKS.md` tracker?
- **Action**: If there is a mismatch, update **ALL** occurrences to the single source of truth.

## 2. Intro/Outro Flow (首尾呼应)
- **Introduction (Opening)**:
    - Does it explicitly mention the **Previous Lesson** by name/concept?
    - Does it explain *why* we are here based on *where* we came from? (e.g., "Now that we have installed Python (L3), let's protect it (L4).")
- **Conclusion (Closing)**:
    - Does it explicitly name the **Next Lesson**?
    - Does it provide a "Cliffhanger" or logical bridge? (e.g., "But how do we save this code? Find out in [Next Lesson Title].")
    - **CRITICAL**: The "Next Lesson Title" used here MUST match the actual title of the next file.

## 3. Cross-Reference Check (文内引用)
- If the lesson refers to a concept from an earlier lesson (e.g., "As we learned in M1L2..."), verify that M1L2 actually covers that concept.
