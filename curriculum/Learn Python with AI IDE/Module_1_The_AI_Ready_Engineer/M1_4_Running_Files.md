# Module 1 Lesson 4: The Scroll (Running Files)

> **Module 1: The Raw Interface**
> 目标：编写并运行你的第一个 Python 脚本文件。

---

## 1. 为什么需耍文件？

REPL (上一课的 `>>>`) 很好，但它是“阅后即焚”的。
真正的软件工程师，是将逻辑刻录在“卷轴”上 —— 也就是 **.py 源代码文件**。
文件通过了**持久化 (Persistence)**，让我们可以反复运行代码，也可以分享给别人。

---

## 2. 编写卷轴 (Creating the File)

在这一步，我们暂时不使用 Antigravity IDE，而是体验一下最原始的文本编辑。
我们需要一个纯文本编辑器。

> **硬核模式 (推荐)**：
> 在终端里直接使用 `nano` 编辑器（大多数 Mac/Linux 自带）。
> 1. 输入 `nano hello.py` 并回车。
> 2. 你会进入一个简陋的编辑界面。

> **普通模式**：
> 使用记事本 (Windows) 或 TextEdit (Mac, 需设为纯文本模式)。
> 新建文件，保存为 `hello.py`。

### 写入代码
无论你用什么工具，请在文件中写下这一行：

```python
print("Hello from a file!")
```

### 保存与退出 (Nano)
如果你用的是 `nano`：
1.  按 `Ctrl + O` (Write Out)，然后回车确认文件名。
2.  按 `Ctrl + X` (Exit) 退出编辑器。

现在，用 `ls` 看一下，你的当前目录下应该多了一个 `hello.py`。

---

## 3. 宣读卷轴 (Running the File)

现在文件有了，怎么运行它？
记住，Shell 是指挥官，Python 是翻译官，`hello.py` 是任务书。

在终端 Shell 提示符 (`$` 或 `>`) 下，输入：

```bash
python hello.py
```

回车。

### 发生了什么？
1.  **Shell** 接到命令，找到了 `python` 程序。
2.  **Shell** 告诉 `python`：“嘿，去读一下 `hello.py` 这个文件。”
3.  **Python** 打开文件，逐行翻译代码 (`print...`) 给 CPU。
4.  **CPU** 执行指令，在屏幕上打印出 "Hello from a file!"。
5.  **结束**：Python 任务完成，退出，把控制权还给 **Shell**。

---

## 4. Module 1 总结：原始的力量

恭喜你，完成了 Module 1。
你现在已经掌握了计算机最底层的交互逻辑：
*   **Terminal/Shell**: 你的指挥舱。
*   **Python Interpreter**: 你的执行引擎。
*   **Files**: 你的任务脚本。

这一切看起来有点简陋，甚至有点麻烦（比如 `nano` 真的很难用）。
这正是为什么我们需要 **IDE**。

在 Module 2 中，我们将把这些零散的工具（终端、编辑器、文件管理器）组装成一艘真正的飞船 —— **Antigravity IDE**。
准备好升级装备了吗？我们 Module 2 见。
