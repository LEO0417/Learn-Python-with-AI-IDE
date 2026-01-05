# Module 1 Lesson 4: 建立实验室：Virtual Environment

> **课程体系：Learn Python with AI IDE**
> **当前模块**：Module 1 - The AI Ready Engineer
> **前修回顾**：在 [M1L3] 中，我们尝试了使用系统自带的 Python“裸奔”，并意识到了这并不安全。
> **本课目标**：构建安全、可复现的 Python 开发环境，理解**虚拟环境 (Virtual Environment)** 的本质。

---

## 1. 为什么不能直接用系统 Python？

想象一下，你的操作系统（Windows/macOS）是一座精密的摩天大楼。
而系统自带的 Python，是支撑这座大楼水电系统的**核心组件**。

*   **风险**：如果你在这个核心组件上随意安装第三方库（比如 install 了一个通过旧版本 Pandas），你可能会无意中破坏系统工具的依赖，导致系统不稳定。
*   **混乱**：Project A 需要 Pandas 1.0，Project B 需要 Pandas 2.0。如果所有项目都公用一个 Python，它们会打架（依赖冲突）。

**工程化解决方案**：**虚拟环境 (Virtual Environment)**。
我们在大楼外，搭建一个个独立的“生化实验室” (Sandbox)。
*   **安全**：实验室炸了也不会影响大楼主体。
*   **隔离**：每个实验室有自己独立的试剂（依赖包）。
*   **可丢弃**：环境玩坏了？删掉重建即可，毫发无损。

我们将使用 **Miniconda**，业界最成熟的环境管理工具。

---

## 2. 准备：验明正身 (Pre-flight Check)

下载软件前，必须确认你的硬件架构。

### 2.1 macOS 用户
点击屏幕左上角的 ** -> 关于本机 (About This Mac)**。
*   **Apple M1/M2/M3...**：架构为 **ARM64** (Apple Silicon)。
*   **Intel Core...**：架构为 **x86_64** (Intel)。

### 2.2 Windows 用户
现代 PC 几乎全是 **x64** 架构。
*   右键“此电脑” -> 属性 -> 确认“64 位操作系统，基于 x64 的处理器”。

---

## 3. 安装：部署 Miniconda

请访问 [Miniconda 官网](https://docs.conda.io/en/latest/miniconda.html) 下载。

### 3.1 Windows 安装关键点 (PATH 策略)
在安装步骤中，你会看到 *"Add Miniconda3 to my PATH environment variable"*。
*   **新手推荐 (勾选)**：虽然安装程序标红警告，但为了让你能直接在 PowerShell 里使用 `conda` 命令，不仅要勾选，而且这会极大地降低后续配置 IDE 的难度。
    *   *注意：如果你电脑里之前装过 Anaconda 或其他 Python，请先通过“设置 -> 应用”卸载干净。*
*   **稳健路线 (不勾选)**：如果你是老手，可以不勾选。但以后每次必须手动从开始菜单打开 "Anaconda Prompt" 才能使用 Conda。

### 3.2 macOS 安装关键点
*   一路“继续”即可。安装完成后，它会自动配置你的 Zsh Shell。
*   **重要**：安装后必须重新打开终端（完全退出再进），才能生效。

---

## 4. 实战：创建你的第一个环境

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
conda create -n ai_course python=3.12 -y
```
*   `-n ai_course`：环境名称。
*   `python=3.12`：指定 Python 版本（兼顾稳定与新特性）。

### 4.3 激活环境 (Activate)
这是最关键的一步。环境建好了，你得进去。
```bash
conda activate ai_course
```

**观察终端变化**：
命令行最左侧的提示符应该从 `(base)` 变成了 **`(ai_course)`**。
只要看到这个 `(ai_course)`，你就在安全的实验室和中了。此时你输入 `python`，调用的就是这个盒子里的 Python，而不是系统的 Python。

---

## 5. 跨平台安全策略 (Windows Only)

Windows PowerShell 默认有一个安全策略，可能会阻止脚本运行。
输入以下命令检查：
```powershell
Get-ExecutionPolicy
```
如果返回 `Restricted`，你需要修改它以便正常开发。
**安全建议**：将策略改为 `RemoteSigned`（Scope: CurrentUser）。
以**管理员身份**运行 PowerShell，输入：
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
*   选择 `Y` 确认。

---

## 6. 工程自检 (Engineering Checkpoint)

本课结束，请务必执行以下验收流程。

### ✅ 验收标准 (Pass Criteria)
1.  **位置隔离**：在激活环境后，输入 `which python` (Mac) 或 `where python` (Win)。
    *   **预期**：路径必须包含 `envs/ai_course`。如果还是 `/usr/bin/python`，说明你还在用系统 Python。
2.  **版本一致**：输入 `python --version`。
    *   **预期**：必须是 `Python 3.12.x`。
3.  **环境列表**：输入 `conda env list`，能看到星号 `*` 指向 `ai_course`。

### 🛑 常见故障 (Fail & Triage)

*   **故障 1**：`conda: command not found`
    *   *原因*：PATH 没配好。
*   **故障 2**：激活后左边没变
    *   *原因*：Shell 初始化问题。输入 `conda init` 然后重启终端。

### 🔄 最小复现与重置 (Recovery)
如果你把 `ai_course` 搞坏了，只需利用虚拟环境的“可丢弃”特性：
```bash
conda deactivate
conda remove -n ai_course --all
conda create -n ai_course python=3.12 -y
```

---

> [!IMPORTANT]
> **本课结语**
>
> 现在，我们拥有了一个干净、安全、隔离的开发环境。
> 你不再是“裸奔”的游击队，而是拥有正规实验室的科学家。
>
> 既然有了实验室，我们以后做的实验（代码）也应该被正规地记录下来，而不是像 REPL 那样随手丢弃。
> **下一课，我们将学习脚本工程，编写持久化的代码。**
