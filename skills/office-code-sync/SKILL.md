---
name: office-code-sync
description: Sync the official Stanford assignments repository into the local `references/office-code/` folder. Use when asked to update official course files, refresh the upstream snapshot, or compare local curriculum against the Stanford source repo.
---

# Office Code Sync

## Overview

将官方仓库 `https://github.com/mihail911/modern-software-dev-assignments` 同步到本项目的 `references/office-code/` 目录，并保证拉取过程可追溯、可回滚。

## Workflow

### 1) 确认目标目录
- 目标目录固定为项目根目录下的 `references/office-code/`。
- 若目录不存在，执行首次克隆。
- 若目录存在，先确认其是否为 git 仓库。

### 2) 初始化子模块（首次使用）
```bash
git submodule update --init --recursive
```

### 3) 更新前检查（目录已存在时）
- 检查是否有未提交修改：
  ```bash
  git -C references/office-code status --porcelain
  ```
- 若有输出，停止更新并询问用户是否要提交/暂存/放弃修改。

### 4) 拉取最新代码（无本地改动时）
```bash
git -C references/office-code fetch origin
git -C references/office-code pull --ff-only
```

### 5) 记录同步信息
- 输出当前版本：
  ```bash
  git -C references/office-code log -1 --oneline
  ```
- 将同步结果写入当日 `docs/WORKLOG/YYYY-MM-DD.md`。

## Notes
- `references/office-code/` 视为官方快照目录，默认不直接修改其中代码。
- 如需做对比或改造，建议复制到其他目录再操作。
