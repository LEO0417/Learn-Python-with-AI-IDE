# Learning Python with AI IDE Week1 Lesson2：终端搭建 Python 环境


## Part 1：这节课的作用与目标
### 学习理念：为什么学环境
- AI 能帮你装库，但环境错了，所有脚本都白费
- 环境是“统一标准”，让你和 AI 在同一套配置上对齐
- 你懂环境，才能知道该让 AI 执行哪些命令、给哪些权限

### 课程目标
- 安装并验证 Miniconda
- 创建并激活 `ai_course` 环境
- 确认 Python 版本是 3.12

### 本课说明
- 同时覆盖 Windows 与 macOS
- 看到“Mac/Linux”就按 Mac 步骤走
- 看到“Windows”就按 Windows 步骤走

## Part 2：安装前的系统检查
### Mac：确认芯片
- 点击左上角苹果图标 → “关于本机”
- 如果看到 Apple M1/M2/M3/M4：下载 Apple Silicon 版
- 如果看到 Intel：下载 Intel 版

### Windows：确认 64 位
- 现代电脑通常是 64 位（x64）
- 记不清也没关系，直接下载 64 位版本

## Part 3：安装 Miniconda
### 下载与安装
- 去官网下载安装包
- Mac：双击 `.pkg`
- Windows：双击 `.exe`
- Windows 如提示 “Add to PATH” 建议勾选

### 命令 1：验证安装（Mac/Linux）
```bash
conda --version
```
- 你应该看到版本号，例如 `conda 23.x.x`
- 如果报错，先关闭终端再打开一次

### 命令 1：验证安装（Windows）
```bat
conda --version
```
- 你应该看到版本号
- 如果报错，先重开 PowerShell

### 如果仍然报错
- Mac：执行 `conda init`，再重开终端
- Windows：重启 PowerShell 或电脑

## Part 4：创建课程目录（在终端里完成）
### 命令 2（Mac/Linux）：创建目录
```bash
mkdir -p ~/ai_course/week1
```
- 没有报错就说明成功

### 命令 3（Mac/Linux）：进入目录
```bash
cd ~/ai_course/week1
```
- 再运行 `pwd`，末尾应出现 `ai_course/week1`

### 命令 2（Windows）：创建目录
```bat
mkdir C:\Users\<你的用户名>\ai_course\week1
```
- 没有报错或提示“已存在”都算成功

### 命令 3（Windows）：进入目录
```bat
cd C:\Users\<你的用户名>\ai_course\week1
```
- 再运行 `cd`，末尾应出现 `ai_course\week1`

## Part 5：创建与激活环境
### 命令 4：创建环境
```bash
conda create -n ai_course python=3.12 -y
```
- 你会看到安装进度条
- 结束后光标回到下一行

### 命令 5：激活环境
```bash
conda activate ai_course
```
- 你应该看到命令行最左边多出 `(ai_course)`

### 命令 6：检查版本
```bash
python --version
```
- 你应该看到 `Python 3.12.x`

### 如果环境没有激活
- 看不到 `(ai_course)`
- `python --version` 不是 3.12
- 解决：再执行一次 `conda activate ai_course`

## Part 6：练习与复盘
### 练习 1：验证 conda
- 输入 `conda --version`
- 看到版本号再继续

### 练习 2：创建并激活环境
- 输入 `conda create -n ai_course python=3.12 -y`
- 输入 `conda activate ai_course`

### 练习 3：确认版本
- 输入 `python --version`
- 看到 `Python 3.12.x`

### 本课复盘
- 我能安装并验证 Miniconda
- 我能创建 `ai_course` 环境并激活
- 我能确认 Python 版本正确
