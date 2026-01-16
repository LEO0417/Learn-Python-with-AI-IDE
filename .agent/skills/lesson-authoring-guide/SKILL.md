---
name: lesson-authoring-guide
description: The master guide for teaching philosophy, lesson structure, and technical standards for the "Learn Python with AI IDE" course. Use this to ensure all new content adheres to the "Professional, Rigorous & Welcoming" tone and the 7-stage lesson structure.
---

# Lesson Authoring Guide (教学行动指南) - V2.0

This skill encapsulates the core teaching philosophy and standards for creating and reviewing curriculum content.

## 1. Teaching Philosophy (教学定位)
- **Tone**: **Professional, Rigorous & Welcoming (专业、严谨且亲切)**.
- **Metaphor Principle**: Use familiar metaphors (e.g., "Workbench", "Plug") to bridge concepts.
- **Combatting the "Curse of Knowledge"**:
    - No "Concept Jumps": Define new terms immediately.
    - No "Label Drift": Use consistent terms for the same actions.
    - No "Implicit Assumptions": Explain underlying physical rules (e.g., file extensions).

## 2. Lesson Structure (7-Stage Logic)
Each lesson should ideally follow this flow:
1.  **Backtrack (前修回顾)**: Connect to the previous lesson.
2.  **Today's Teaser (今日预告)**: Establish motivation.
3.  **Core Meaning (核心逻辑/机制)**: Explain the "Why" and "How" it works.
4.  **Practical Practice (操作与练习)**: Hands-on steps.
5.  **Efficiency Tips (提亮/进阶)**: IDE tricks or shortcuts.
6.  **Checkpoint (自测与验收)**: Clear pass criteria.
7.  **Summary & Next Stop (复盘与预告)**: Bridge to the next lesson.

## 3. Technical Standards
- **Python Version**: 3.13.
- **Environment**: `ai_course` (via Miniconda).
- **Localization**: STRICT adherence to regional terminology (SC vs TC).
    - SC: 终端, 变量, 文件夹.
    - TC: 終端機, 變數, 資料夾.

## 4. Content Locking & Immortality (定稿锁定准则)
- **Freeze Rule**: Once the USER declares a lesson as **FINALIZED (定稿)**, that lesson and ALL preceding lessons (L1 to current) enter a "Frozen State".
- **Modification Ban**: AI must not modify or propose changes to frozen documents unless specifically requested by the USER to "Unlock" or "Refactor" them.
- **Dependency Handling**: Future lessons must adapt to the definitions and logic established in the frozen foundations, not the other way around.
- **Current Status**: Lessons **M1L1 through M1L7** are now considered **FINALIZED**.

## 5. Metadata Header
Every lesson must start with:
```markdown
# Module {X} Lesson {Y}: {Title}

> **课程体系：Learn Python with AI IDE**
> **当前模块**：Module {X} - {ModuleName}
> **本课目标**：[Goal description]

---
```
