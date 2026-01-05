# Module 1 Lesson 2: 工程第一步：建立隔离的开发环境

> **课程体系：Learn Python with AI IDE**
> **当前模块**：Module 1 - The AI Ready Engineer
> **前修回顾**：在 [M1L1] 中，我们建立了“工程探索”的思维。
> **本课目标**：构建安全、可复现的 Python 开发环境，理解 System Python 与 Virtual Environment 的本质区别。

---

## 1. 原理：为什么不能直接用系统 Python？

很多新手常犯的一个错误是：直接在电脑自带的 Python 上安装各种软件包。
想象一下，你的操作系统（Windows/macOS）是一个精密的仪器，而系统自带的 Python 是维持这个仪器运转的**核心组件**。

*   **macOS/Linux**：系统底层工具（如 `yum`, `dnf` 或一些 GUI 工具）严重依赖特定版本的 Python。
*   **Windows**：虽然系统依赖较少，但如果你把所有库（Pandas, Django, PyTorch）都装在一个全局环境里，很快就会遇到**“依赖地狱” (Dependency Hell)** —— Project A 需要 Pandas 1.0，Project B 需要 Pandas 2.0，二者无法共存。

**工程化解决方案**：**虚拟环境 (Virtual Environment)**。
我们在系统之外，搭建一个个独立的“沙盒”。
*   **安全**：沙盒里的操作绝不影响系统。
*   **隔离**：每个项目有自己独立的依赖清单。
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
*   **新手推荐 (勾选)**：虽然安装程序标红警告，但为了让你能直接在 PowerShell 或 IDE 终端里使用 `conda` 命令，建议勾选。
    *   *注意：如果你电脑里之前装过 Anaconda 或其他 Python，请先通过“设置 -> 应用”卸载干净，否则会冲突。*
*   **稳健路线 (不勾选)**：如果你是老手，可以不勾选。但以后每次必须手动从开始菜单打开 "Anaconda Prompt" 才能使用 Conda。

### 3.2 macOS 安装关键点
*   一路“继续”即可。安装完成后，它会自动配置你的 Zsh Shell。
*   安装后重新打开终端，如果看到 `(base)` 字样，说明成功。

---

## 4. 实战：创建你的第一个环境

打开你的终端（Windows 用户推荐用 PowerShell，Mac 用户用 Terminal）。

### 4.1 验证安装
输入：
```bash
conda --version
```
*   **成功信号**：输出 `conda 24.x.x` 或类似版本号。
*   **失败信号**：`command not found` 或 `无法识别 terms...`。
    *   *Windows 修复*：重启电脑，或者检查环境变量 PATH。

### 4.2 创建环境 (Create)
输入以下指令（精确输入）：
```bash
conda create -n ai_course python=3.12 -y
```
*   `-n ai_course`：环境名称。
*   `python=3.12`：指定 Python 版本（兼顾稳定与新特性）。
*   `-y`：自动确认所有安装询问。

### 4.3 激活环境 (Activate)
这是最关键的一步。环境建好了，你得进去。
```bash
conda activate ai_course
```

**观察终端变化**：
命令行最左侧的提示符应该从 `(base)` 变成了 **`(ai_course)`**。
只要看到这个 `(ai_course)`，你就处于安全沙盒中。

---

## 5. 跨平台安全策略 (Windows Only)

Windows PowerShell 默认有一个安全策略，可能会阻止脚本运行。
输入以下命令检查：
```powershell
Get-ExecutionPolicy
```
如果返回 `Restricted`，你需要修改它以便正常开发。
**安全建议**：将策略改为 `RemoteSigned`（允许本地脚本，远程脚本需签名）。
以**管理员身份**运行 PowerShell，输入：
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
*   选择 `Y` 确认。
*   *注意：不要使用 `Unrestricted`，那会让你的电脑裸奔。*

---

## 6. 工程自检 (Engineering Checkpoint)

本课结束，请务必执行以下验收流程。

### ✅ 验收标准 (Pass Criteria)
在终端中依次输入以下 3 条命令，若输出符合预期，则通过：

1.  **检查 Python 位置**：
    *   命令：
        *   Mac/Linux: `which python`
        *   Windows: `where python`
    *   **预期**：路径中必须包含 `envs/ai_course` 字样。如果路径是 `C:\Python312\...` 或 `/usr/bin/python`，说明你**没激活环境**。

2.  **检查版本**：
    *   命令：`python --version`
    *   **预期**：`Python 3.12.x`。

3.  **环境列表**：
    *   命令：`conda env list`
    *   **预期**：能在列表中看到 `ai_course`，并且有一颗星号 `*` 标记在它前面。

### 🛑 常见故障 (Fail & Triage)

*   **故障 1**：`conda: command not found`
    *   *原因*：PATH 没配好，或者没重开终端。
    *   *对策*：Windows 重装勾选 PATH；Mac 运行 `source ~/.zshrc`。
*   **故障 2**：`Activate` 后左边没变
    *   *原因*：Shell 没有正确初始化。
    *   *对策*：运行 `conda init`，然后完全关闭并重启终端。
*   **故障 3**：`SSLError` / 网络连接超时
    *   *原因*：国内网络连接 Anaconda 官方源受阻。
    *   *对策*：搜索“Conda 换清华源”，配置 `.condarc` 文件镜像。

### 🔄 最小复现与重置 (Recovery)
如果你把环境搞乱了（比如装了错误的包），不要慌，直接重建：
```bash
conda deactivate                 # 1. 退出
conda remove -n ai_course --all  # 2. 删除
conda create -n ai_course ...    # 3. 重建
```

---

> [!IMPORTANT]
> **本课结语**
>
> 你现在拥有的不仅仅是 Python，而是一套**“防污染”**的工业开发体系。
> 很多初学者的编程热情就熄灭在这一步。恭喜你，你已经越过了第一道也是最难的一道技术门槛。
>
> **下一课，我们将深入这个“黑框框”，学习如何用命令行主宰你的文件系统。**
