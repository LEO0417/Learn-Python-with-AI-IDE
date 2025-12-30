---
name: lesson-scaffold
description: Build or refactor lessons for the two-track curriculum (Learn Python with AI IDE + Stanford CS146S) into the “讲义 + 练习” format. Use when creating a new lesson, rewriting Stanford week content, adding exercises, or updating `docs/MAPPING.md`, `docs/WEEK1_TASKS.md`, and `docs/WORKLOG/*.md`.
---

# Lesson Scaffold

## Overview

Provide a consistent workflow to design lesson structure, write exercises, and keep mapping/tasks/logs in sync for the two-track curriculum.

## Workflow

### 1) Clarify scope
- Identify track: `curriculum/Learn Python with AI IDE` (main track) or `curriculum/Stanford CS146S` (support track).
- Identify target week/lesson and the source file(s) to refactor.
- Confirm expected output location and any required cross-links.
- Reference sources: `references/office-code/` (official code) and `references/ng_lesson/` (parallel course).

### 2) Draft lesson skeleton
- Use the standard “讲义 + 练习” frame, keep sections minimal and practical.
- Include the smallest runnable example and its expected output.

```markdown
# 课程标题

## 课程目标
- ...

## 关键概念
- 概念 1：定义 + 常见误区

## 演示与拆解
- 最小示例
- 逐行解释

## 练习
- 练习 1（复现）
- 练习 2（改写）
- 练习 3（迁移）

## 复盘清单
- 我能运行并得到预期输出
- 我能解释关键语句
- 我能改写并通过自测
```

### 3) Write exercises
- Provide 2-3 exercises per concept: reproduce → modify → transfer.
- Add a concrete “运行后看到什么” for each exercise.
- Keep inputs/output simple and verifiable.

### 4) Update cross-links
- Update `docs/MAPPING.md` with the new lesson mapping or status.
- Update `docs/WEEK1_TASKS.md` if tasks are completed or re-scoped.
- Append a short note to today’s `docs/WORKLOG/YYYY-MM-DD.md`.

### 5) Quality checks
- Ensure terms and names are consistent across tracks.
- Ensure code blocks are runnable and outputs are deterministic.
- Ensure the lesson matches the target audience (zero baseline).
