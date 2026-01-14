---
name: lesson-scaffold
description: Build or refactor lessons for the Mainline 1 (Module-based) or Mainline 2 curriculums. Use when creating new lessons, ensuring they adhere to the "Professional & Rigorous" tone and standard structure.
---

# Lesson Scaffold

## Overview

Provide a consistent workflow to design lesson structure for the **Module-based** curriculum (Mainline 1) and the Stanford Companion (Mainline 2).

## Workflow

### 1) Clarify scope
- **Refer to Single Source of Truth**: You **MUST** read `docs/MAPPING.md` to identify the required knowledge points and alignment with the Andrew Ng curriculum.
- **Track**: `Mainline 1` (Foundation, Module 1-4) or `Mainline 2` (Stanford Application).
- **Module/Lesson**: e.g., `M1_2` (Module 1 Lesson 2).
- **Reference**: Also check `references/ng_lesson/` for source material.

### 2) Draft lesson skeleton
- **Tone**: Professional, Rigorous, Welcoming.
- **Structure**:

```markdown
# Module X Lesson Y: [Title]

> **课程体系：Learn Python with AI IDE**
> **当前模块**：Module X - [Module Name]
> **本课目标**：[Goal description]

---

## 1. 🔙 Backtrack (前修回顾)
- [Review concept from previous lesson]

## 2. 📅 Today's Teaser (今日预告)
- [Why this matters, motivation]

## 3. 🏗️ Core Meaning (核心逻辑/机制)
- [Explanation of the "Why" and underlying physics]

## 4. 🛠️ Practical Practice (操作与练习)
```bash
# Code or commands
```

## 5. 🔥 Efficiency Tips (提亮/进阶)
- [IDE shortcuts or productivity hacks]

## 6. ✅ Checkpoint (自测与验收)
- [Pass criteria]

## 7. 🔄 Summary & Next Stop (复盘与预告)
- [Summary and bridge to next lesson]
```

### 3) Quality checks
- **Tone Check**: Are there any childish metaphors ("magic", "nest")? -> Remove them.
- **Logic Check**: Is the "Why" explained before the "How"?
- **Terminology Audit**: Check for SC/TC differences if applicable (e.g., 资源管理器 vs 檔案總管).
- **Link Check**: Are cross-references to other Modules valid?

### 4) Update documentation
- Update `docs/MAPPING.md` status.
- Update `docs/WORKLOG/`.
