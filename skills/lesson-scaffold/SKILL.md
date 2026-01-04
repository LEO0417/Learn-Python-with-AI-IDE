---
name: lesson-scaffold
description: Build or refactor lessons for the Mainline 1 (Module-based) or Mainline 2 curriculums. Use when creating new lessons, ensuring they adhere to the "Professional & Rigorous" tone and standard structure.
---

# Lesson Scaffold

## Overview

Provide a consistent workflow to design lesson structure for the **Module-based** curriculum (Mainline 1) and the Stanford Companion (Mainline 2).

## Workflow

### 1) Clarify scope
- **Track**: `Mainline 1` (Foundation, Module 1-4) or `Mainline 2` (Stanford Application).
- **Module/Lesson**: e.g., `M1_2` (Module 1 Lesson 2).
- **Reference**: Check `docs/MAPPING.md` and `references/ng_lesson/`.

### 2) Draft lesson skeleton
- **Tone**: Professional, Rigorous, No Metaphors.
- **Structure**:

```markdown
# Module X Lesson Y: [Title]

> **Module X: [Module Name]**
> 目标：[One sentence goal]

---

## 1. Philosophy/Why (理论)
- 为什么学这个？
- 解决什么工程问题？
- (Optional) 对比传统模式 vs AI 模式。

## 2. The Raw Logic (机制)
- 底层发生了什么？(e.g., CPU, Memory, Shell, Interpreter)
- 破除黑盒，讲解原理。

## 3. Instruction (指令)
```bash
# 具体命令或代码
```
- 逐步执行。

## 4. Practice (硬核练习)
- 练习 1：[Action] -> [Expected Output]
- 练习 2：[Action] -> [Expected Output]
```

### 3) Quality checks
- **Tone Check**: Are there any childish metaphors ("magic", "nest")? -> Remove them.
- **Logic Check**: Is the "Why" explained before the "How"?
- **Link Check**: Are cross-references to other Modules valid?

### 4) Update documentation
- Update `docs/MAPPING.md` status.
- Update `docs/WORKLOG/`.
