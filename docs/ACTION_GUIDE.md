# 教学行动指南 (Action Guide) - V2.0

本指南用于统一教学理念、内容结构与落地流程，适用于两条主线的全部课程建设与复盘。

## 1. 教学定位 (Philosophy)
- **受众**：希望以正统、严肃方式掌握 AI 时代编程能力的初学者。
- **基调**：**严肃、硬核、专业 (Professional & Rigorous)**。
    - 拒绝低幼化隐喻（如“婴儿”、“魔法棒”）。
    - 强调“精确性”与“逻辑判断力”。
    - 将学员视为未来的工程师或 AI 协作指挥官。
- **目标**：不只是“跑通代码”，而是建立对计算机底层（终端、解释器）与顶层（AI IDE）的完整认知。

## 2. 课程体系 (Curriculum Tracks)
### Learn Python with AI IDE (基础课)
- **架构**：**Module 制**（非 Week 制）。
- **内容**：分两大阶段。
    - **Module 1**: 从“原声终端”到“AI IDE 工作流”。建立工程基座。
    - **Module 2**: 在 AI IDE 辅助下系统学习 Python 核心体系（对齐 Ng 课程）。
- **目录**：`curriculum/Learn Python with AI IDE/Module_X_.../`

### Stanford CS146S (配套演练)
- **架构**：**Week 制**（跟随 Stanford 进度）。
- **内容**：基于斯坦福 CS146S 的**配套讲义**。
- **目标**：应用基础技能，构建 Agent、RAG 等实际 AI 应用。
- **目录**：`curriculum/Stanford CS146S/weekX/`

## 3. 课程结构标准 (Lesson Structure)
每节课名为 `M{Module}_{Sequence}_{Topic}.md`（如 `M1_2_Terminal_Basics.md`），需包含：

1.  **Philosophy/Why (理论)**：为什么学这个？解决什么工程问题？
2.  **The Raw Logic (机制)**：底层发生了什么？（如 Shell 如何调用 Python）
3.  **Instruction (指令)**：具体的命令或代码。
4.  **Practice (硬核练习)**：不只是复现，要求在终端/IDE 中实际操作并验证结果。

## 4. 映射与维护 (Mapping)
- **核心映射**：基础课程的 Module 知识点需映射参考 **Andrew Ng** 的 Python 课程 (Module 1 & 2)。
- **文档维护**：
    - `docs/MAPPING.md`: 维护基础课程与 Ng 课程的知识点对照。
    - `docs/MODULE_TASKS.md`: 追踪 Module 建设进度。

## 5. 术语规范 (Terminology)
- 统一使用英文术语 + 中文解释。例如：`Terminal (终端)`, `Interpreter (解释器)`, `Repository (仓库)`。
- IDE 统一称为 **Antigravity** 或 **AI IDE**。
- 引用斯坦福课程时，使用 **CS146S**。

## 6. 完成标准 (Definition of Done)
- 风格检查：无低幼隐喻，逻辑严密。
- 闭环验证：所有命令/代码在无前置假设的环境下可运行。
- 知识对齐：覆盖 Ng 课程对应的核心技术点。
