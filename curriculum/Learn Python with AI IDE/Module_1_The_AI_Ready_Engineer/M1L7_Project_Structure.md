# Module 1 Lesson 7: 你的数字蓝图：工程结构与路径管理

> **课程体系：Learn Python with AI IDE**
> **当前模块**：Module 1 - The AI Ready Engineer
> **前修回顾**：在 [M1L6] 中，我们掌握了 IDE。
> **本课目标**：从单文件脚本升级为**项目 (Project)**。理解“工作区”概念，掌握绝对稳健的路径处理方法 (`pathlib`)，并学会保护敏感数据。

---

## 1. 为什么不能把所有文件堆在桌面？

新手常把图片、代码、数据全都混在一个文件夹里，甚至直接放在桌面上。
这在工程中是不可接受的。

**项目 (Project)** = 代码 + 数据 + 配置 + 文档。
一个健康的 AI 项目结构应该像这样：

```text
my_ai_project/
├── data/               # 存放 CSV, JSON 等数据文件
├── assets/             # 存放图片、音频
├── src/                # 存放源代码 (.py)
├── .env                # [机密] 存放 API Keys
├── .gitignore          # 告诉 git 忽略哪些文件
├── requirements.txt    # 依赖说明书
└── main.py             # 入口文件
```
IDE 打开的应该是 `my_ai_project` 这个根目录，而不仅仅是 `main.py`。这就是 **Workspace (工作区)** 的概念。

---

## 2. 核心痛点：路径漂移问题

在 M1L5 中我们提到，Python 默认通过 CWD (当前工作目录) 寻找文件。
但这个 CWD 是不可靠的。
*   如果你在终端里 `cd src` 然后运行 `python main.py`，你的 CWD 就是 `src`。
*   如果你点击 IDE 播放按钮，IDE 可能会把 CWD 设置为项目根目录。

**结果**：你的代码 `open("data/file.csv")` 在一种情况下能跑，另一种情况下报错 "File not found"。

**工程解决方案**：**基于锚点的路径构建**。
我们不再依赖“当前在哪里”，而是依赖“文件本身在哪里”。

---

## 3. 实战：使用 Pathlib 构建稳健路径

Python 3 引入了 `pathlib`，这是现代路径处理的标准库。

### 3.1 实验准备
1.  在项目根目录下新建一个文件夹 `utils`。
2.  在 `utils` 里新建脚本 `path_test.py`。
3.  输入以下代码：

```python
from pathlib import Path

# 1. 获取当前脚本的绝对路径 (Anchor)
current_file = Path(__file__).resolve()
print(f"当前脚本路径: {current_file}")

# 2. 获取当前脚本所在的目录 (Parent)
current_dir = current_file.parent
print(f"当前脚本目录: {current_dir}")

# 3. 构建指向兄弟文件的路径
# 假设我们要找 utils 平级目录 data 下的 config.json
# 逻辑：当前目录 -> 父级(根目录) -> data -> config.json
project_root = current_dir.parent
target_file = project_root / "data" / "config.json"
print(f"目标文件路径: {target_file}")
```

**原理**：
*   `__file__`：永远指向脚本自身。这是一个物理锚点，不会随你从哪里启动程序而改变。
*   `/` 操作符：在 `pathlib` 中，斜杠被重载为路径拼接符，Windows/Mac 通用。

---

## 4. 安全红线：敏感数据隔离

在 AI 开发中，你经常需要使用 API Key (如 OpenAI Key)。
**绝对禁止**将 Key 直接写在代码里（e.g., `api_key = "sk-..."`）。
尤其是当你稍后学习 Git 时，这一行代码会让你的 Key 泄露给全世界。

### 4.1 `.env` 文件
我们使用一个名为 `.env` 的纯文本文件来存储机密。
```text
OPENAI_API_KEY=sk-xxxxxx
DB_PASSWORD=secret
```

### 4.2 `.gitignore` 防护网
在项目根目录创建一个名为 `.gitignore` 的文件，写入：
```text
.env
__pycache__/
*.log
```
这告诉版本控制系统：**“永远无视这些文件，绝对不要把它们上传到 GitHub。”**

---

## 5. 工程自检 (Engineering Checkpoint)

### ✅ 验收标准 (Pass Criteria)
1.  **路径复现**：无论你在终端里 `cd` 到哪里，运行你的 `path_test.py`，打印出的“目标文件路径”都应该是完全一致的绝对路径。
2.  **结构规范**：你的练习项目不应该再是单文件，至少包含一个子文件夹。
3.  **安全意识**：你的项目根目录下是否有 `.gitignore`？里面是否包含了 `.env`？

### 🛑 常见故障 (Fail & Triage)
*   **故障 1**：`NameError: name 'Path' is not defined`
    *   *原因*：忘了 `from pathlib import Path`。
*   **故障 2**：`Path(__file__)` 报错
    *   *原因*：在 REPL 中无法使用 `__file__`，因为它没有文件载体。必须在脚本中运行。
*   **故障 3**：Windows 下路径显示为 `C:\\Users\\...` 不好看
    *   *解释*：这是正常的。Python 内部会自动处理反斜杠转义。只要 `Path` 对象能打印出来，它就是对的。

---

> [!IMPORTANT]
> **本课结语**
>
> 很多初级程序员写代码只能在自己的电脑上跑，换个位置就崩。
> 使用 `pathlib` 和规范的目录结构，你的代码将获得**可移植性 (Portability)**。
>
> **下一课，我们将介绍陪伴你探索新大陆的终极伙伴 —— AI Sidebar Agent。**
