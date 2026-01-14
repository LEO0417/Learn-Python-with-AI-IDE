# 教学行动指南（最高版本）

本指南用于统一教学理念、内容结构与落地流程，适用于统一主线课程及其配套实践案例的建设与复盘。

## 1. 教学定位
- 受众：零基础学习者，对 IDE、终端无概念，中文为主。
- 目标：通过项目导向学习，理解核心概念与逻辑，能读懂并复现项目。
- 核心能力：读懂代码、运行代码、改写代码、复盘过程。

## 2. 统一主线 + 实践案例
- 主线（Learn Python with AI IDE）：为零基础提供完整知识铺垫，覆盖 Python + 终端 + AI IDE + Ollama + NG 相关基础。
- 实践案例（Stanford CS146S）：作为实践课程案例，用于复现实战代码与理念，不再作为独立主线。
- 维护：主线与实践案例的对应关系在 `docs/MAPPING.md` 中维护。

## 3. 叙述风格与结构
- 风格：讲义 + 练习，避免口播稿式叙事。
- 表达：短句、分层、概念先行；每个概念必须配最小示例。
- 连贯性：统一术语与命名（如环境名、工具名、模型名）。

## 4. 单课模板（建议）
- 课程目标（学完能做什么）
- 关键概念（术语、心智模型、常见误区）
- 演示与拆解（最小可运行示例 + 逐行解释）
- 练习（从仿写到改写到迁移）
- 复盘清单（学员自检）

## 5. 练习设计原则
- 由浅入深：先复现，再改写，最后迁移到小任务。
- 可验证：每个练习明确“运行后看到什么输出”。
- AI 协作：鼓励使用 AI 解释、定位报错、生成变体，但必须写出自己的改动。

## 6. 素材与引用
- Stanford 官方代码以 `references/office-code/` 为准，课程讲义撰写时必须对照官方实现。
- `curriculum/Case Studies/Stanford CS146S/` 内以讲义与课程材料为主，不作为官方代码来源。
- `references/ng_lesson/` 作为并行参考，优先补齐主线课程的 Python 基础。
- `references/` 目录为官方/参考快照，除非来自官方更新，否则禁止手动修改。
- 引用时标注文件路径，避免无出处的信息拼贴。

## 7. 文件与命名规范
- 课程主线：`curriculum/Learn Python with AI IDE/`。
- 实践案例：`curriculum/Case Studies/Stanford CS146S/`（暂含 week1-week2）。
- 官方代码：`references/office-code/`（官方仓库快照）。
- 文档中心：`docs/`，包含行动指南、映射表、任务清单、工作日志。
- 本地技能：`skills/`，存放课程编排与维护用的 Codex 技能。
- 旧内容：`curriculum/Learn Python with AI IDE/legacy/` 视为历史素材，不再作为新主线模板。

## 8. 完成标准（Definition of Done）
- 课程具备可复现步骤（命令、文件、预期结果）。
- 术语一致，跨文档不冲突。
- 练习可独立完成并有答案检验方式。
- 映射表已更新，课程与实践案例互引完整。

## 9. 本地技能索引
- `lesson-scaffold`：`skills/lesson-scaffold/SKILL.md`，用于将课程内容整理为“讲义 + 练习”格式，并同步映射表、任务清单与工作日志。
- `office-code-sync`：`skills/office-code-sync/SKILL.md`，用于同步官方仓库到 `references/office-code/` 目录。
- `ng-lesson-sync`：`skills/ng-lesson-sync/SKILL.md`，用于同步 DeepLearning.AI ng_lesson 官方课件到 `references/ng_lesson/`。

## 10. 更新流程
- 每日更新 `docs/WORKLOG/`。
- 每次新增或调整课程内容，必须同步更新映射表与任务清单。
- 每周复盘一次结构与进度，修正偏差。

## 11. `references/ng_lesson/` 手动同步流程
- 同步前确认官方页面与范围（记录 URL 与日期）。
- 对比本地与官方内容差异，标出新增/修改点。
- 仅在确认是官方更新时同步到 `references/ng_lesson/`。
- 在当日 `docs/WORKLOG/YYYY-MM-DD.md` 记录同步范围、来源 URL、差异摘要。
- 可使用 `skills/ng-lesson-sync/scripts/ng_lesson_sync.py` 自动化同步（需登录 cookie）。
