# Module 1 Lesson 2: 系统验明正身与环境配置 (Environment Setup)

> **Module 1: The AI-Ready Engineer**
> **目标**：构建工业级 Python 开发环境，理解系统架构差异，确保“环境一致性”。

---

## 1. 理论：为什么环境配置是“第一课”？

在软件工程界有一个著名的笑话：“但在我的电脑上能跑啊！” (Works on my machine!)。

这句话背后隐藏的是灾难。不同的操作系统、不同的 Python 版本、散乱的第三方库依赖，会让你的代码在他人电脑或服务器上运行失败。

为了解决这个问题，我们要建立 **Virtual Environments (虚拟环境)**。
*   **隔离性**：不同项目的依赖互不干扰。
*   **可移植性**：别人可以一键复刻你的运行环境。
*   **安全性**：即使你把虚拟环境弄乱了，删掉重建即可，不会破坏你的操作系统。

本课中，我们将使用工业标准的 **Miniconda** 来管理这一切。

---

## 2. 第一阶段：验明正身 (System Check)

在下载任何软件之前，你必须搞清楚你的底层硬件架构。如果下载了错误的指令集版本，性能将大幅下降甚至无法启动。

### 2.1 macOS 用户：Apple Silicon 还是 Intel？
1.  点击屏幕左上角的 **苹果图标 ()**。
2.  选择 **关于本机 (About This Mac)**。
3.  查看 **芯片 (Chip)** 这一行：
    *   **Apple M1/M2/M3/M4**：你是 ARM64 架构（即 Apple Silicon）。你需要对应 ARM64 的软件。
    *   **Intel Core/Xeon**：你是 x86_64 架构。你需要对应 x64 的软件。

### 2.2 Windows 用户：64 位是标配
现代 Windows 电脑几乎全是 **x64** (x86_64) 架构。
1.  右键点击“此电脑”或“我的电脑”。
2.  选择 **属性**。
3.  确认“系统类型”为“64 位操作系统，基于 x64 的处理器”。

---

## 3. 第二阶段：安装 Miniconda (魔法手杖)

**Conda** 是目前数据科学和 AI 工程领域事实上的包管理标准。我们将安装轻量级的 **Miniconda**。

### 3.1 下载与安装路径
请访问 [Miniconda 官网](https://docs.conda.io/en/latest/miniconda.html) 或使用国内清华源镜像。
*   **Mac M 芯片**：选择 `macOS Apple M1 64-bit pkg`。
*   **Win 平台**：选择 `Windows 64-bit exe`。

### 3.2 Windows 安装特别注意
在安装过程中，你会遇到一个勾选项：*"Add Miniconda3 to my PATH environment variable"*。
> [!CAUTION]
> 虽然安装程序标红提示“不推荐”，但为了后续能直接在终端（Command Prompt/PowerShell）调用 Conda，**我们建议勾选此项**。
> 如果你没有勾选，你以后必须通过“Anaconda Prompt”来启动终端，这会增加操作复杂度。

---

## 4. 第三阶段：创建专属房间 (Creating Environment)

现在我们要用终端咒语，在你的电脑里变出一个**“AI 基础课专用房间”**。

### 4.1 终端初体验
*   **Mac 用户**：按 `Cmd + Space` 搜索 `Terminal` 并打开。
*   **Windows 用户**：按 `Win` 键搜索 `PowerShell` 并在窗口右键选择“以管理员身份运行”。

### 4.2 验证 Conda
在黑框框里输入：
```bash
conda --version
```
如果输出 `conda 23.x.x` 字样，说明安装成功。

### 4.3 创建环境
输入以下精确指令：
```bash
conda create -n ai_course python=3.12 -y
```
**指令解析**：
*   `create`：指令动词，创建。
*   `-n ai_course`：设定环境名称为 `ai_course`。
*   `python=3.12`：指定这个房间里只安装 Python 3.12 版本（这是目前最稳定的版本之一）。
*   `-y`：静默安装，不需要你反复点击确认。

---

## 5. 第四阶段：激活与燃料注入 (Activation)

### 5.1 走进房间
环境造好了，我们要进去：
```bash
conda activate ai_course
```
**观察变化**：
你会发现你的命令行最左侧出现了一个小括号 `(ai_course)`。
**记住：只要看到这个括号，你就是安全的。** 你在这个状态下安装的任何库，都不会影响到系统底层的核心稳定。

### 5.2 查看家具 (List Installed Tags)
输入：
```bash
conda list
```
你会看到 Python 3.12 已经静静地躺在那里。

---

## 6. 第五阶段：对接 IDE (Driver Configuration)

最后，我们需要让 **Antigravity IDE** 知道我们的新房间在哪里。

1.  **打开 Antigravity**。
2.  **呼出命令面板**：
    *   Mac: `Cmd + Shift + P`
    *   Win: `Ctrl + Shift + P`
3.  **输入指令**：`Python: Select Interpreter`。
4.  **选择识别**：在弹出的列表里，仔细寻找写着 `ai_course` 的那一行。
    *   它通常长这样：`Python 3.12.x ('ai_course': conda)`。
5.  **状态确认**：观察 IDE 的右下角状态栏。如果显示了 `3.12.x ('ai_course')`，恭喜你，对接成功！

---

## 7. 硬核练习

1.  **环境毁灭与重生**：
    不要怕弄坏电脑。尝试在终端中执行 `conda deactivate` 退出房间，然后尝试用 `conda remove -n ai_course --all` 手动删掉这个环境。再按照本课教程重新创建一遍。
    **目的**：消除你对“配环境”的恐惧。环境是可以随时抛弃重来的。
2.  **跨系统认知**：
    如果你使用的是 Windows，请在 PowerShell 中输入 `Get-ExecutionPolicy`。如果返回 `Restricted`，你需要询问 AI 如何更改权限以便平滑运行 Conda。

---

> [!IMPORTANT]
> **本课总结**：
> 到这一步，你已经拥有了一套标准、干净、可维护的开发环境。
> **不要小看“配环境”。** 很多自学者在这一关就被劝退了。能撑过这一课，说明你具备了成为工程师的基本耐心。
>
> **下一课，我们将正式深入这个黑框框，学习如何用命令行主宰你的文件系统。**
