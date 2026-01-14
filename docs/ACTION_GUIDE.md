# 教学行动指南 (Action Guide) - V2.0

本指南用于统一教学理念、内容结构与落地流程，适用于两条主线的全部课程建设与复盘。

## 1. 教学定位 (Philosophy)
- **受众**：希望以正统、严肃方式掌握 AI 时代编程能力的初学者。
- **基调**：**严肃、硬核、专业 (Professional & Rigorous)**。
    - **隐喻原则**：使用接地气的隐喻（如“微信”、“生化实验室”），但必须有铺垫。若无铺垫，优先使用直白描述，拒绝突兀的概念（如突然出现的“驾驶舱”）。
    - **初学者视角 (Beginner Mindset)**：
        - **打破“知识诅咒”**：不要机械地假设用户不懂“术语”，而是要**严格审视“上下文依赖”**。
        - **零前置假设**：任何在**当前课程之前的已定稿课程 (L1...N-1)** 中未出现的概念，对于用户来说都是“天书”。必须默认为 0 认知。
        - **处理法则**：若必须使用未铺垫概念，必须当场进行“降维打击”（用生活隐喻解释）并给予定心丸（预告后续详解）。
    - 强调“精确性”与“逻辑判断力”。
    - 将学员视为未来的工程师或 AI 协作指挥官。
- **目标**：不只是“跑通代码”，而是建立对计算机底层（终端、解释器）与顶层（AI IDE）的完整认知。
    - **生存优先**：在涉及终端/交互的课程中，必须教授“生存技巧”（如 `Ctrl+C` 紧急刹车、历史记录回溯），消除初学者的恐惧感。
    - **核心工程**：用“核心工程能力 (Core Engineering)”替代过于营销化的“工业级 (Industrial-grade)”表述。
    - **一致性与回顾 (Consistency & Recall)**：
        - **定稿不可变 (Immutable Foundation)**：已定稿课程（目前为 M1L1, M1L2, M1L3）被视为只读基座。严禁修改其定义好的課程順序或核心概念。任何新內容必須適配既定路徑，而不能要求前文配合修改。
        - 新修改的内容必须与已定稿课程的用词严格保持一致。
        - 在引入新概念时，必须显式回顾引用的前序知识点（如 M1L3 需回顾 M1L2 的 Path 概念），建立知识链条。

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
