---
description: Sync and update the local Secret Usage Guide with new insights.
---
# /ug (Update Guide)

Usage: `/ug`

Steps:
1. **Insight Harvesting**: Use the `project-identity` skill (Knowledge Management rules) to scan the conversation for technical and agentic insights.
2. **Sanitization**: Anonymize any personal paths or sensitive data discovered.
3. **Update Document**: Refine or append to `docs/使用指南/Agent_Usage_Guide.md` with the new findings.
4. **Internal Sync**: Verify the guide remains excluded from Git.
5. **Report**: Give a bilingual summary of what was added.
