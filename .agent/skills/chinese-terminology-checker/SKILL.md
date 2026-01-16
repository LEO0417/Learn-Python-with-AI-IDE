# Chinese Terminology Checker Skill

This skill ensures terminology consistency between Simplified Chinese (SC) and Traditional Chinese (TC) lesson files. It prevents regional terminology leakage (e.g., using Taiwan terms in Mainland Chinese lessons).

## Objectives
1.  Maintain a strict mapping between SC and TC terms.
2.  Ensure SC files use Mainland China technical terms.
3.  Ensure TC files use Taiwan technical terms.
4.  Standardize project-specific terminology.

## Glossary Reference
See [GLOSSARY.md](./GLOSSARY.md) for the authoritative mapping.

## Instructions
1.  When editing an SC file (`*.md`), never use TC terms like "檔案總管", "終端機", "資料夾", "專案".
2.  When editing a TC file (`*_TW.md`), never use SC terms like "资源管理器", "终端", "文件夹", "项目".
3.  Use the `grep_search` tool to check for forbidden terms if unsure.
4.  Update [GLOSSARY.md](./GLOSSARY.md) whenever a new term is introduced or corrected.

## Verification Step
Before finishing a task that involves both SC and TC versions:
- Check if term 'A' in SC is term 'B' in TC according to the glossary.
- Ensure no regional "shibboleths" are leaked into the wrong version.
