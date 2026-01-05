# Module 1 Lesson 4: 建立实验室：Virtual Environment (Conda)

> **课程体系：Learn Python with AI IDE**
> **当前模块**：Module 1 - The AI Ready Engineer
> **本课目标**：构建安全、可复现的 Python 开发环境，理解**虚拟环境 (Virtual Environment)** 的隔离本质。

---

## 1. 为什么不能直接用系统 Python？

想象一下，你的操作系统（Windows/macOS）是一座精密的摩天大楼。
而我们上一课在终端里看到的那个 `python`（系统自带），是支撑这座大楼水电系统的**核心基础设施**。

**为什么要建立虚拟环境？因为“生化隔离”。**

*   **危险的操作**：作为初学者，你会频繁安装各种 AI 库（numpy, torch）。如果你直接把这些装在系统 Python 里，一旦版本冲突，可能会导致系统基础工具（如 yum, brew 或系统设置）崩溃。
*   **版本打架**：Project A 需要 Python 3.8，Project B 需要 Python 3.12。如果只有一个环境，它们根本法共存。

**工程化解决方案**：我们在大楼外，搭建一个个独立的“生化实验室” (Sandbox)。
*   **安全**：实验室炸了也不会影响系统大楼。
*   **独立**：每个项目一个实验室，互不干扰。
*   **可丢弃**：环境玩坏了？删掉重建即可，毫发无损。

我们将使用 **Miniconda**，它是业界最成熟、最轻量的环境管理工具。

---

## 2. 准备：验明正身 (Pre-flight Check)

下载软件前，必须确认你的硬件架构，否则装上了也跑不起来。

### 🍎 macOS 用户
点击屏幕左上角的 ** -> 关于本机 (About This Mac)**。
*   **Apple M1/M2/M3...**：架构为 **ARM64** (Apple Silicon)。请下载 **macOS Apple Silicon** 版。
*   **Intel Core...**：架构为 **x86_64** (Intel)。请下载 **macOS Intel x86** 版。

### 🪟 Windows 用户
现代 PC 几乎全是 **x64** 架构。
*   右键“此电脑” -> 属性 -> 确认“64 位操作系统，基于 x64 的处理器”。

---

## 3. 安装：部署 Miniconda

我们推荐 **Miniconda** 而不是 Anaconda。前者只有 50MB（纯净），后者有 600MB（臃肿）。

请访问 [Miniconda 官网下载页](https://docs.conda.io/en/latest/miniconda.html) 下载对应的安装包。

### 3.1 Windows 安装关键点 (PATH 策略)
在安装步骤中，你会看到红色的警告 *"Add Miniconda3 to my PATH environment variable"*。
*   **新手强烈推荐 (勾选)**：虽然安装程序可能会吓唬你，但为了让你能直接在 PowerShell 里使用 `conda` 命令，**请务必勾选它**。这会极大地降低新手配置 IDE 的难度。
    *   *注意：如果你电脑里之前装过 Anaconda 或其他 Python，建议先卸载干净再安装 Miniconda。*

### 3.2 macOS 安装关键点
*   下载 `.pkg` 安装包，一路“继续”即可。
*   **重要**：安装完成后，**必须关闭并重新打开终端**，才能让环境变量生效。

---

## 4. 实战：通过终端管理环境

打开你的终端（Mac Terminal / Win PowerShell）。

### 4.1 验证安装
输入：
```bash
conda --version
```
*   **成功信号**：输出 `conda 24.x.x` 或类似版本号。
*   **失败信号**：`command not found`。
    *   *Mac*：试试运行 `source ~/.zshrc`。
    *   *Windows*：重启电脑。

### 4.2 创建环境 (Create)
建立我们的第一个实验室名为 `ai_course`：
```bash
conda create -n ai_course python=3.10 -y
```
*   `-n ai_course`：给实验室取个名字。
*   `python=3.10`：指定这个实验室配备 Python 3.10 版本（AI 领域目前最稳定的版本）。

### 4.3 激活环境 (Activate)
这是最关键的一步。环境建好了，你得**进去**。
```bash
conda activate ai_course
```

**观察终端变化**：
命令行最左侧的提示符应该从 `(base)` 变成了 **`(ai_course)`**。
*   `(base)`：默认的大厅，不要在这里装东西。
*   `(ai_course)`：你的私人实验室。此时输入 `python`，调用的就是这个盒子里的 Python。

---

## 5. 跨平台安全策略 (Windows Only)

**Windows 用户请注意**：PowerShell 默认可能会阻止 `conda` 脚本运行。如果你遇到“禁止运行脚本”的红色报错：

1.  用**管理员身份**运行 PowerShell。
2.  输入以下“解封”指令：
    ```powershell
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
3.  输入 `Y` 并回车确认。
4.  关闭管理员窗口，重新打开普通 PowerShell 即可。

---

## 6. 工程自检 (Engineering Checkpoint)

本课结束，请务必执行以下验收流程。

### ✅ 验收标准 (Pass Criteria)
1.  **位置隔离**：在激活 `(ai_course)` 后，输入 `which python` (Mac) 或 `where python` (Win)。
    *   **预期**：路径里必须包含 `.../envs/ai_course/...`。
    *   *Fail*：如果路径里还是 WindowsApps 或者 `/usr/bin/python`，说明你没激活成功。
2.  **版本一致**：输入 `python --version`。
    *   **预期**：必须是 `Python 3.10.x`。
3.  **环境列表**：输入 `conda env list`，能看到星号 `*` 指向 `ai_course`。

### 🔄 最小复现与重置 (Recovery)
如果你把 `ai_course` 搞坏了，只需利用虚拟环境的“可丢弃”特性：
```bash
# 1. 先退出来
conda deactivate
# 2. 连锅端删掉
conda remove -n ai_course --all
# 3. 重新建一个
conda create -n ai_course python=3.10 -y
```

---

> [!IMPORTANT]
> **本课结语**
>
> 现在，我们拥有了一个干净、安全、隔离的开发环境。
> 你不再是“裸奔”的游击队，而是拥有正规实验室的科学家。
>
> 既然有了实验室，我们以后做的实验（代码）也应该被正规地记录下来，而不是像 REPL 那樣随手丢弃。
> **下一课：脚本工程 —— 从对话到写作。**
