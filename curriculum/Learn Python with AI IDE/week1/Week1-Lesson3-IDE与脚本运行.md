# Learning Python with AI IDE Week1 Lesson3：IDE 与脚本运行


## Part 1：这节课的作用与目标
### 学习理念：为什么学 IDE 与运行
- AI 能生成代码，但你必须能在 IDE 里验证它能否运行
- IDE 是“观察点”，你在这里看输出、报错、修改效果
- 你会用 IDE，才谈得上指挥 AI 改哪、跑哪、怎么回滚

### 课程目标
- 打开项目目录并安装 Python 插件
- 选择 `ai_course` 解释器
- 在 IDE 和终端里运行脚本
- 学会用 `pip` 安装一个依赖

### 本课说明
- 同时覆盖 Windows 与 macOS
- 看到“Mac/Linux”就按 Mac 步骤走
- 看到“Windows”就按 Windows 步骤走

## Part 2：打开项目与插件安装
### 打开项目目录
- 在 IDE 中选择 “Open Folder”
- 选中你之前创建的 `ai_course/week1`
- 你应该看到左侧文件树出现 `week1`

### 安装 Python 插件
- 打开插件市场
- 搜索 `Python`
- 点击 Install
- 看到“已安装”再继续

## Part 3：选择解释器
### 选择解释器
- 打开命令面板：`Cmd+Shift+P` / `Ctrl+Shift+P`
- 输入并选择：`Python: Select Interpreter`
- 选择带 `ai_course` 的那一项
- 你应该看到右下角显示 `ai_course`

### 如果看不到 `ai_course`
- 先回终端执行 `conda activate ai_course`
- 再回 IDE 重新选择解释器

## Part 4：第一段脚本（IDE 里跑起来）
### 新建文件
- 在左侧空白处右键 → New File
- 文件名输入：`hello.py`

### 写入代码
```python
print("Hello, AI IDE!")
```

### 运行方式 A：IDE 运行
- 点击右上角 Run
- 你应该在下方终端看到 `Hello, AI IDE!`

### 运行方式 B：终端运行（Mac/Linux）
```bash
python hello.py
```
- 你应该看到 `Hello, AI IDE!`

### 运行方式 B：终端运行（Windows）
```bat
python hello.py
```
- 你应该看到 `Hello, AI IDE!`

## Part 5：安装依赖（为以后做准备）
### 什么是依赖
- 依赖就是别人写好的工具库
- 以后你要用 AI、读文件、画图，都要装依赖

### 命令 1：升级 pip
```bash
python -m pip install --upgrade pip
```
- 看到安装完成提示再继续

### 命令 2：安装一个示例依赖
```bash
python -m pip install ollama
```
- 看到 “Successfully installed” 就成功

### 命令 3：查看已安装列表
```bash
python -m pip list
```
- 你应该能看到 `ollama` 在列表里

## Part 6：练习与复盘
### 练习 1：IDE 中创建并运行脚本
- 创建 `hello.py`
- 运行并看到 `Hello, AI IDE!`

### 练习 2：终端中运行脚本
- 在终端执行 `python hello.py`
- 看到同样的输出

### 练习 3：安装并确认依赖
- 执行 `python -m pip install ollama`
- 再执行 `python -m pip list`

### 本课复盘
- 我能在 IDE 中打开项目并选择解释器
- 我能在 IDE 和终端里运行脚本
- 我能用 pip 安装依赖
