# Learning Python with AI IDE Week1 Lesson4：综合演练


## Part 1：这节课的作用与目标
### 学习理念：为什么要综合演练
- AI 可能帮你跳过步骤，但你需要完整路径来掌控结果
- 综合演练把“知道”和“能做”打通，避免只会看不会做
- 能完整走一遍流程，你才知道该授权 AI 做到哪一步

### 课程目标
- 能从打开终端开始，完成环境准备
- 能在 IDE 中创建并运行脚本
- 能写出第一行 Python 代码并看到输出

### 本课说明
- 同时覆盖 Windows 与 macOS
- 看到“Mac/Linux”就按 Mac 步骤走
- 看到“Windows”就按 Windows 步骤走

## Part 2：从零开始的完整流程（一步一步走）
### 步骤 1：打开终端
- Mac：`Cmd + Space` → 搜索 `Terminal`
- Windows：开始菜单 → 搜索 `PowerShell`
- 看到光标在闪，就算成功

### 步骤 2：确认当前位置
```bash
pwd
```
- Windows 用户可直接输入 `cd`
- 如果你看到自己的用户名，就继续

### 步骤 3：进入课程目录（Mac/Linux）
```bash
cd ~/ai_course/week1
```
- 如果报错，说明目录还没建

### 步骤 3：进入课程目录（Windows）
```bat
cd C:\Users\<你的用户名>\ai_course\week1
```
- 如果报错，说明目录还没建

### 步骤 4：如果目录不存在，就创建它（Mac/Linux）
```bash
mkdir -p ~/ai_course/week1
```
- 创建后再执行一次 `cd ~/ai_course/week1`

### 步骤 4：如果目录不存在，就创建它（Windows）
```bat
mkdir C:\Users\<你的用户名>\ai_course\week1
```
- 创建后再执行一次 `cd C:\Users\<你的用户名>\ai_course\week1`

### 步骤 5：激活环境
```bash
conda activate ai_course
```
- 你应该看到 `(ai_course)`

### 步骤 6：确认 Python 版本
```bash
python --version
```
- 你应该看到 `Python 3.12.x`

## Part 3：用 IDE 跑通第一行代码
### 步骤 7：打开 IDE
- 选择 “Open Folder”
- 打开 `ai_course/week1` 目录

### 步骤 8：选择解释器
- `Cmd+Shift+P` / `Ctrl+Shift+P`
- 选择 `Python: Select Interpreter`
- 选中 `ai_course`

### 步骤 9：新建 `hello.py`
- 右键 → New File
- 输入 `hello.py`

### 步骤 10：写入第一行代码
```python
print("Hello, AI IDE!")
```

### 步骤 11：运行
- 点 Run 或在终端执行 `python hello.py`
- 看到 `Hello, AI IDE!` 就成功

## Part 4：加一个函数，让脚本更像程序
### 步骤 12：新建 `demo_func.py`
- 右键 → New File
- 输入 `demo_func.py`

### 步骤 13：写一个函数
```python
def greet(name):
    return f"你好，{name}！"

print(greet("小林"))
```

### 步骤 14：运行
```bash
python demo_func.py
```
- 你应该看到 `你好，小林！`

## Part 5：本课复盘
- 我能从终端开始，完成环境准备
- 我能在 IDE 中写代码并运行
- 我能写出第一行 Python 代码并看到输出
- 我能写出一个最小函数并调用
