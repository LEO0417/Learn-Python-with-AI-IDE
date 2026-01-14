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

### 2) 准备上游快照（本地临时目录）
- 使用临时目录进行同步，例如：`/tmp/office-code-upstream`。
```bash
git clone https://github.com/mihail911/modern-software-dev-assignments /tmp/office-code-upstream
```

### 3) 更新前检查（目录已存在时）
- 若 `references/office-code/` 有本地改动，先手动备份或复制一份。
- 可选：与临时目录做快速对比：
  ```bash
  diff -rq references/office-code /tmp/office-code-upstream
  ```

### 4) 拉取最新代码（更新临时目录）
```bash
git -C /tmp/office-code-upstream fetch origin
git -C /tmp/office-code-upstream reset --hard origin/master
```

### 5) 记录同步信息
- 输出当前版本：
  ```bash
  git -C /tmp/office-code-upstream log -1 --oneline
  ```
- 将同步结果写入当日 `docs/WORKLOG/YYYY-MM-DD.md`。

### 6) 覆盖本地快照
- 使用 `rsync` 同步（会删除本地多余文件）：
  ```bash
  rsync -a --delete --exclude .git /tmp/office-code-upstream/ references/office-code/
  ```
- 若无 `rsync`，可先备份再覆盖：
  ```bash
  rm -rf references/office-code/*
  cp -R /tmp/office-code-upstream/* references/office-code/
  ```

## Notes
- `references/office-code/` 视为官方快照目录，默认不直接修改其中代码。
- `references/` 目录仅在官方更新时改动，禁止手动修改。
- 如需做对比或改造，建议复制到其他目录再操作。
