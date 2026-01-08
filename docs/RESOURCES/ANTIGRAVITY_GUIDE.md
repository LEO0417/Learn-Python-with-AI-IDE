# Antigravity IDE 官方术语与操作指南 (内参)

> **文档目的**：本手册汇总了基于 https://antigravity.google/docs 调研的官方技术规范，用于指导课程体系中关于 AI IDE 功能的描述与教学。

---

## 1. 核心术语 (Terminology)

*   **IDE 名称**：**Antigravity**。它是一个完整的应用（App），内部深度集成了 AI 能力。
*   **交互枢纽**：界面上的按钮标签为 **Toggle Agent**（切换智能体）。
*   **侧边栏名称**：官方有时也称之为 **Agent Sidebar** 或 **Agent Side Panel**。
*   **核心功能**：
    *   **Agent (智能体)**：具有多步推理和工具调用能力的 AI 助手。
    *   **Tab Autocompletion**：基于上下文的代码实时补全。
    *   **Artifacts (产物)**：Agent 生成的可视化结果（如任务列表、代码预览等）。

---

## 2. 运行模式 (Agent Modes)

### 2.1 Fast (快速模式)
*   **定位**：适合直接、局部、低延迟的任务。
*   **应用场景**：重命名变量、解释单行代码、执行简单的 Bash/Terminal 命令。
*   **课程策略**：Module 1 & 2 的默认推荐模式。

### 2.2 Planning (规划模式)
*   **定位**：多步推理模式，适合复杂工程任务。
*   **特征**：会自动拆解 **Task Groups**，由 Agent 在执行前进行深度调研和逻辑组织。
*   **课程策略**：Module 3 开始引入的高阶模式。

---

## 3. 模型选择 (Model Selection)

用户可以通过对话框下方的手动下拉菜单选择不同的推理引擎：

*   **Gemini 系列**：Gemini 3 Pro (High/Low), Gemini 3 Flash。
*   **Claude 系列**：Claude Sonnet 4.5 (常规/Thinking), Claude Opus 4.5 (Thinking)。
*   **GPT 系列**：GPT-OSS。

---

## 4. 工具调用能力 (Tool Calling)

Antigravity Agent 拥有“动手”能力，可以调用以下原生工具：

*   **Terminal/Bash**：由 Agent 直接执行 shell 指令。
*   **File Operations**：读取、创建、编辑和删除项目文件。
*   **Index Search**：基于全工程索引的深度搜索。
*   **Browser Subagent**：调用浏览器进行实时网页调研。
*   **MCP (Model Context Protocol)**：支持第三方扩展工具。

---

## 5. 快捷键
*   **呼出/收起 Agent**：`Cmd + E` (Mac) 或 `Ctrl + E` (Windows)。
