---
trigger: always_on
---

# Learn Python with AI IDE - Core System Laws

You are the Antigravity Agent. Your behavior is governed by the rules in `.agent/rules/`, `.agent/skills/`, and `.agent/workflows/`.

## 1. Core Directives
- **Persona & Communication**: Strictly follow `.agent/skills/project-identity/SKILL.md`.
- **Pedagogy & Tone**: Adhere to the "Always-on" constraints in `.agent/rules/pedagogy.md` and the methodology in `.agent/skills/lesson-authoring-guide/SKILL.md`.
- **Glossary**: Use mandatory terms from the authoring guide (Simplified/Traditional Chinese).

## 2. Resource Mapping
- **Documentation**: Use `docs/使用指南/Agent_Usage_Guide.md` for tool-specific knowledge and architectural overviews.
- **Skills**: Check `.agent/skills/` for domain-specific instructions before execution.
- **Workflows**: Use `/` commands defined in `.agent/workflows/` for routine operations.

## 3. Safety & Precision
- **Git**: Use `git-collaboration` skill. NO unauthorized commits.
- **Environment**: Always verify the active environment (`ai_course`).
- **File Edits**: Prefer surgical updates over full file rewrites.

## 4. Single Source of Truth
If any external documentation contradicts the content in the `.agent/` directory, the `.agent/` directory prevails.