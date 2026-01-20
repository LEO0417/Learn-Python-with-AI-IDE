# Project State & Curriculum Map (项目全景)

> **Status**: Live Tracking
> **Last Updated**: 2026-01-20

This document serves as the **Single Source of Truth (SSOT)** for the project's progress, curriculum structure, and external mappings.

---

## 📊 1. Progress Overview (进度总览)

| Module | Name | Status | Completion |
| :--- | :--- | :--- | :--- |
| **M1** | The AI-Ready Engineer | **DONE** | 100% (10/10 Lessons) |
| **M2** | Python Foundation | **PLANNING** | 0% (Target: Align with Ng) |
| **M3** | Stanford Bridge | **PENDING** | 0% |
| **CS146S** | Stanford Case Studies | **DOING** | Week 1 In Progress |

---

## 📚 2. Finalized Curriculum (M1: The AI-Ready Engineer)

**Target**: Mac/Windows users, absolute beginners.
**Theme**: "From Fear to Mastery" - Building the Standard Workbench.

| Sequence | ID | Title | Core Concept | Status |
| :--- | :--- | :--- | :--- | :--- |
| 01 | M1L1 | **Why Code?** | Philosophy, Confidence, "AI as Lever" | ✅ Final |
| 02 | M1L2 | **Terminal Mastery** | Shell, `ls`, `cd`, `mkdir`, "No Fear" | ✅ Final |
| 03 | M1L3 | **Python REPL** | Interactive Python, Math, Variables | ✅ Final |
| 04 | M1L4 | **Environment Setup** | Conda, `ai_course`, Isolation | ✅ Final |
| 05 | M1L5 | **Script Engineering** | `.py` files, VS Code Basics, Code Runner | ✅ Final |
| 06 | M1L6 | **What Is IDE** | The "Cockpit", Extensions, Configuration | ✅ Final |
| 07 | M1L7 | **The Standard Workbench** | Folder Structure, `data/`, `scripts/` | ✅ Final |
| 08 | M1L8 | **AI Sidebar Agent** | Chat, Context (`@`), README writing | ✅ Final |
| 09 | M1L9 | **Human-AI Loop** | The "Review" Step, Handling AI errors | ✅ Final |
| 10 | M1L10 | **Module Review** | "Audit", Full Recap, Road to M2 | ✅ Final |

---

## 🛠️ 3. task Tracker (开发任务表)

### Module 2: Python Foundation (Pending)
*Target: Align with Andrew Ng's "AI Python for Beginners"*

*   [ ] **Plan**: Map M2 structure to Ng's 4 Modules (Basics, Automation, Files, Data).
*   [ ] **Experiment**: Create "ImportError" lab to teach environment binding (System vs. `ai_course`).
*   [ ] **Tooling**: Introduce `Indent-Rainbow` and `Error Lens`.

### Case Studies: Stanford CS146S (实战案例复现)
*遵循“Learning Python by building AI tools”逻辑，将 Module 1/2 的基础能力落到实战。*

| Week | Goal | Core Task | Status |
| :--- | :--- | :--- | :--- |
| **W1** | 终端环境/IDE 闭环 + 提示词入门 | 跑通 `hello.py`；完成 6 个提示词脚本 TODO | **DOING** |
| **W2** | 逻辑与决策自动化 | 对应 Stanford Week 2 (待细化) | PENDING |
| **W3** | 结构化数据处理 | 对应 Stanford Week 3 | PENDING |
| **W4-8** | 异步、API 与工程化集成 | 依次对接 Stanford 高阶课程 | PENDING |

**当前细化任务**:
*   [x] **W1D5**: Ollama setup & Python script chat (Reviewing `references/office-code`)
*   [ ] **W1D6**: AI Programming Basics (Lists, Dicts, Logic)
*   [ ] **W1D7**: Prompt Engineering (K-Shot)
*   [ ] **W1D8**: CoT (Chain of Thought)

---

## 🔗 4. External Mapping (对标吴恩达课程)

We align our **Module 2** with Andrew Ng's **"AI Python for Beginners"** to ensure industry-standard coverage.

| Our Course | Ng Module | Ng Topic | Status |
| :--- | :--- | :--- | :--- |
| **M1L9** (Loop) | M1-L4 | Running your first program | Covered |
| **M2-L?** (Logic) | M1-L6 | Data in Python (Lists/Dicts) | Todo |
| **M2-L?** (Vars) | M1-L8 | Variables | Todo |
| **CS146S-W1** | M2-L6 | Helping AI make decisions | Todo |
| **CS146S-W1** | M1-L9 | Building LLM Prompts | Todo |

---
*Note: This file replaces `FINALIZED_LESSONS_TITLES.md`, `MODULE_TASKS.md`, and `MAPPING.md`.*
