# Module 1 Lesson 5: 脚本工程：编写持久化代码

> **课程体系：Learn Python with AI IDE**
> **当前模块**：Module 1 - The AI Ready Engineer
> **前修回顾**：在 [M1L4] 中，我们发现 REPL 虽然快，但无法保存。
> **本课目标**：从“对话”转向“脚本”。理解 Python 文件执行流程，掌握基本的脚本编写与运行工作流。

---

## 1. 为什么我们需要脚本 (Script)？

REPL 是阅后即焚的。
在真实的工程中，特别是当你第二天要继续昨天的代码，或者你需要让代码在服务器上自动跑一个月时，你需要**持久化 (Persistence)**。

**Python 脚本 (.py)** = 固化在硬盘上的逻辑序列。
*   **可复现**：每次运行，逻辑顺序绝对一致。
*   **可维护**：可以随时打开修改，可以进行版本控制。
*   **可批处理**：一个文件可以包含 1000 万行代码，瞬间执行完毕。

---

## 2. 核心机制：执行流程

当你输入 `python mission.py` 时，你其实触发了一连串接力：

1.  **Shell (副官)**：收到命令。在系统 PATH 中找到 `python` 程序。
2.  **Kernel (引擎)**：Python 启动。
3.  **Loading (填弹)**：Python 从硬盘**读取** `mission.py` 的内容。
4.  **Execution (发射)**：从第 1 行执行到最后 1 行。
5.  **Shutdown (熄火)**：执行完毕，Python 进程自动退出，释放内存。

**关键点**：这解释了为什么你每次修改代码后必须**保存 (Save)**。因为 Python 读的是硬盘里的文件，不是你编辑器里还没保存的草稿。

---

## 3. 实战：创建与运行

虽然我们有了 IDE，但为了理解“代码即文本”的本质，我们先用最简单的方式操作一次。

### 3.1 建立目录
打开终端，确保环境激活 `(ai_course)`。
```bash
cd ~  # 回家
mkdir python_scripts
cd python_scripts
```

### 3.2 编写代码
你不需要专门的编程软件。**任何文本编辑器**都可以写代码。
*   Windows 用户：打开记事本 (Notepad)，输入代码，另存为 `runner.py` (注意选“所有文件”，不要存成 .txt)。
*   Mac 用户：打开文本编辑 (TextEdit)，输入代码。(记得转换为纯文本格式)。
*   **推荐 (可选挑战)**：直接用终端编辑器 `nano`（如果你还没准备好，可以跳过，直接用 VS Code 创建文件）。

**代码内容**：
```python
print("--- 自动化脚本启动 ---")

fuel = 100
cost = 30
remaining = fuel - cost

print("初始燃料:", fuel)
print("消耗:", cost)
print("剩余:", remaining)

print("--- 任务完成 ---")
```
将文件保存为 `runner.py`。

### 3.3 运行前的检查 (Pre-flight)
这是无数新手卡住的地方：**“找不到文件”**。
在运行之前，必须先确认文件真的在那里。

输入：
*   Mac/Linux: `ls`
*   Windows: `ls` (PowerShell) 或 `dir` (CMD)

**验收**：你必须在列表里看到 `runner.py`。如果没看到，说明你现在不在正确的文件夹里。请重新 `cd`。

### 3.4 启动！
```bash
python runner.py
```
**观察**：屏幕上应该按顺序打印出 4 行文字。

---

## 4. 常见工程故障 (Troubleshooting)

### 4.1 "No such file or directory"
*   **现象**：`python: can't open file 'runner.py': [Errno 2] No such file or directory`
*   **原因**：Shell 当前的工作目录 (CWD) 和文件所在的目录不一致。
*   **修复**：先用 `ls` 确认文件存在，再运行。或者用绝对路径 `python /Users/leo/python_scripts/runner.py`。

### 4.2 沉默的脚本
*   **现象**：程序跑完了，屏幕上什么都没显示。
*   **原因**：你在脚本里写了 `1 + 1`，但没写 `print(1 + 1)`。
*   **原理**：REPL 会自动打印，但脚本默认是**沉默**的。只有显式的 `print()` 才会向控制台输出内容。

### 4.3 忘记保存 (The "Ghost Code")
*   **现象**：改了代码，运行结果却是旧的。
*   **原因**：编辑器里没保存 (Ctrl+S)。Python 读的是旧文件。
*   **铁律**：**改动 -> 保存 -> 运行**。

---

## 5. 工程自检 (Engineering Checkpoint)

### ✅ 验收标准 (Pass Criteria)
1.  **文件确认**：在运行 Python 前，能使用 `ls` 或 `dir` 确认目标文件存在。
2.  **执行**：运行脚本后，能看到预期的文本输出。
3.  **迭代**：修改脚本中的数字（比如把 fuel 改成 200），**保存**，再次运行，结果发生变化。

### 🛑 常见故障 (Fail & Triage)
*   **故障 1**：`SyntaxError: invalid character` (Mac 用户常见)
    *   *原因*：你可能用了“富文本”编辑器（如 Word 或 TextEdit 的默认模式），导致代码里夹杂了看不见的格式符。
    *   *对策*：务必使用纯文本编辑器 (VS Code, Notepad, Sublime)。
*   **故障 2**：`ModuleNotFoundError`
    *   *原因*：脚本名和系统库重名了（比如你把文件命名为 `math.py` 或 `code.py`）。
    *   *对策*：永远不要用 Python 标准库的名字命名你的脚本。改个名试试。

---

> [!IMPORTANT]
> **本课结语**
>
> 恭喜，你已经掌握了软件工程最基本的一个原子操作：**编写逻辑 -> 保存文件 -> 执行验证**。
>
> 无论多么复杂的 AI 系统（如自动驾驶、ChatGPT 训练管线），本质上都是成千上万个这样的 `.py` 文件在按照特定顺序执行。
>
> 现在的开发方式（记事本+命令行）虽然硬核，但效率太低。
> **下一课，我们将装备重型武器：IDE (集成开发环境)，让这个过程快 10 倍。**
