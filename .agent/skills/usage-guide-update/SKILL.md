---
name: usage-guide-update
description: Specialized skill for managing and updating the internal Hacker Guide (Agent_Usage_Guide.md) with technical and agentic insights.
---

# Usage Guide Update Skill

## 1. Goal
To capture "non-business" technical insights (e.g., model behaviors, IDE quirks, folder structures, credit management) and persist them in the project's private guide.

## 2. Capture Logic
When the user invokes `/ug`, the Agent must:
- **Scan Conversation**: Look for "lightbulb moments" or technical explanations provided during the session.
- **Filter**: Exclude lesson content, curriculum plans, or business logic. Focus on "How the Agent works".
- **Anonymize**: Always convert absolute local paths (e.g., `/Users/leowang/...`) to generic paths (e.g., `~/...`) to maintain portability and privacy.

## 3. Formatting Standards
- **Bilingual**: Use the "English & Chinese" format for section headers and complex technical points.
- **Markdown Hierarchy**: Maintain the existing structure of `docs/使用指南/Agent_Usage_Guide.md`.
- **Bullet Points**: Use concise, action-oriented bullet points for tips and tricks.

## 4. Safety
- **Keep Private**: Ensure the file remains in `.gitignore`.
- **No Overwrite**: Always attempt to append or refine sections rather than deleting existing knowledge.
