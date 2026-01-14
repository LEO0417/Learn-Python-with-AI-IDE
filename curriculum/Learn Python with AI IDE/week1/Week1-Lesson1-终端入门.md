# Learning Python with AI IDE Week1 Lesson1：终端入门


## Part 1：这节课的作用与目标
### 学习理念：为什么学终端
- AI 可以替你敲命令，但你要能判断它在做什么、做没做对
- 终端是“授权入口”：你决定什么时候让 AI 执行、执行什么
- 终端是“审计窗口”：你能看见输出、定位错误、复盘过程
- 学终端不是为了手敲，而是为了掌控全流程

### 课程目标
- 能在 Mac/Windows 打开终端
- 认识终端提示符与光标
- 会用 3 个基本命令：`pwd`、`ls/dir`、`cd`

### 本课说明
- 同时覆盖 Windows 与 macOS
- 看到“Mac/Linux”就按 Mac 步骤走
- 看到“Windows”就按 Windows 步骤走

## Part 2：打开终端（从 0 到 1）
### Mac：打开终端
- 按 `Cmd + Space` 打开聚焦搜索
- 输入 `Terminal`
- 按回车
- 你应该看到一个黑色（或深色）的窗口，光标在闪

### Windows：打开终端
- 点击开始菜单
- 搜索 `PowerShell` 或 `Windows Terminal`
- 点击打开
- 你应该看到一个蓝色/黑色的窗口，光标在闪

### 终端长什么样
- 你会看到一行提示符
- Mac 可能像：`username@MacBook ~ %`
- Windows 可能像：`PS C:\Users\YourName>`
- 光标在闪 = 电脑在等你输入命令

## Part 3：第一个命令（看看我在哪）
### 命令 1（Mac/Linux）：`pwd`
```bash
pwd
```
- 作用：显示你现在的位置（路径）
- 你应该看到一行路径，比如 `/Users/leo`
- 我期待你能读出最后一段名字（这就是当前目录）

### 命令 1（Windows）：`cd`
```bat
cd
```
- 作用：显示你现在的位置（路径）
- 你应该看到一行路径，比如 `C:\Users\leo`
- 我期待你能看到自己的用户名

## Part 4：第二个命令（看看这里有什么）
### 命令 2（Mac/Linux）：`ls`
```bash
ls
```
- 作用：列出当前目录里的文件/文件夹
- 你应该看到一排名字（可能带颜色）
- 如果看到 `Desktop` 或 `Downloads`，说明你在用户目录

### 命令 2（Windows）：`dir`
```bat
dir
```
- 作用：列出当前目录里的文件/文件夹
- 你应该看到很多行，带日期和文件名
- 这很正常，别怕它长

## Part 5：第三个命令（进入一个目录）
### 命令 3（Mac/Linux）：`cd Desktop`
```bash
cd Desktop
```
- 作用：进入桌面目录
- 如果没有报错，就说明成功
- 现在你再输一次 `pwd`，末尾应出现 `Desktop`

### 命令 3（Windows）：`cd Desktop`
```bat
cd Desktop
```
- 作用：进入桌面目录
- 如果没有报错，就说明成功
- 现在你再输一次 `cd`，末尾应出现 `Desktop`

### 回到上一级（可选）
```bash
cd ..
```
- 作用：返回上一级目录
- 你应该看到路径回到上一层
- 如果你迷路了，就先回上一级

## Part 6：练习与复盘
### 练习 1：确认当前位置
- 运行 `pwd`（Mac/Linux）或 `cd`（Windows）
- 把看到的路径读一遍

### 练习 2：列出文件
- 运行 `ls`（Mac/Linux）或 `dir`（Windows）
- 找到 `Desktop` 或 `Downloads`

### 练习 3：进入桌面再回来
- 运行 `cd Desktop`
- 再运行 `pwd` 或 `cd`
- 最后运行 `cd ..` 回到上一层

### 本课复盘
- 我能打开终端并看到光标
- 我能用命令看见当前路径
- 我能列出文件，并进入一个目录
- 我不再害怕黑色窗口
