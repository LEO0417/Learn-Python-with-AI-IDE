# Module 1 Pedagogy & Manifesto (第一章教学心法)

> **Parent Doc**: [Course Design Philosophy](../COURSE_DESIGN_PHILOSOPHY.md)
> **Goal**: To align the "Director's Cut" vision for Module 1 content creation.

## 1. Student Persona & Mental State (学生画像)
*   **State**: **Anxious & Disoriented**. They see the terminal as a dangerous "Black Box" that might break their computer.
*   **Need**: **Safety & Grounding**. They need to feel that everything is "Reverse-able" (可逆) and "Physical" (files exist on disk, not just in the IDE).
*   **Our Stance**: "You cannot break this. If you do, we just delete the folder and start over."

## 2. Knowledge Boundaries (知识边界 - Clean Room)
*   **Strict Containment**: We write L(N) assuming the student **ONLY** knows L1 to L(N-1).
*   **No Concept Drift**: Do not introduce terms like "git commit", "pull request", "classes", or "APIs" unless explicitly taught or necessary for the strictly defined metaphors.
*   **No "Stack" Jumping**: Do not assume knowledge of web stacks, servers, or cloud unless it's the specific topic.

## 3. The "Timeless Workflow" Philosophy (以"道"御"术")
*   **Context**: AI tools evolve weekly. A button in the screenshot today might move tomorrow.
*   **The Teaching Goal**: Do not just teach "Click the blue button". Teach the **Interaction Pattern**:
    1.  **Context (Provide)**: Tell the AI *what* to look at (`@file`).
    2.  **Prompt (Ask)**: State intent clearly.
    3.  **Diff (Review)**: Verify the proposed change.
    4.  **Apply (Commit)**: Accept the change into the codebase.
*   **Mindset vs. Automation**: We teach manual `@` actions not because automation (Vector DBs/Skills) isn't there, but because **explicit control builds an interaction mindset**. Students should feel "in charge" of the context.
*   **The Context Hierarchy**:
    1.  **Active Focus**: What's open in the editor is default.
    2.  **Explicit Reference**: The `@` symbol for multi-file or specific tasks.
    3.  **Conversation History**: Previous prompts and outputs in the current thread.
    4.  **Background Knowledge**: Code Tracker/Skills/RAG.
*   **Disclaimer**: We must explicitly tell students: "The UI will change. The logic of collaboration will not."

## 4. Portraying the AI Agent (Antigravity/AIDE)
*   **Avoid outdated limits**: Do not say "It only sees the active tab".
*   **Accurate but Managed Truth**:
    *   *Reality*: The Agent can access open files, selected code, project structure, terminal output, and potentially more.
    *   *Teaching version*: "The Agent is context-aware. It perceives what you focus on, and you can guide its attention using tools like `@`."
*   **Role**: It is a **Co-pilot / Junior Partner**. It is capable but requires a Captain (User) to approve decisions.

## 5. Lesson Layout: Standard Bookends + Organic Middle
To maintain a unified look and feel while ensuring a narrative flow, every lesson must follow this structure:

### **The Bookends (Fixed Format)**
- **Header**: `# Module X Lesson Y: Title`
- **Metadata Block**: Standard block with Curriculum, Module, and Lesson Objectives.
- **Section 1**: `### 🔙 前修回顾`
- **Section 2**: `### 📅 今日预告`
- **Separator**: `---`

### **The Organic Middle**
- Avoid rigid, numbered headers like "3. Core Meaning" or "4. Practice".
- Use descriptive, narrative-driven headers (e.g., `### 协作的配置：让 AI 听你的`) that transition naturally.

### **The Closing (Fixed Format)**
- **Separator**: `---`
- **Section 3**: `### 💡 结语：[Mindset-oriented Recap Title]`
    *   *Constraint*: Avoid mechanical bullet points. Focus on the "State of Mind" change or a high-level engineering philosophy.
- **Section 4**: `## 下次课程预告：[Seamless Narrative Title]`
    *   *Constraint*: The transition should be seamless, continuing the "story" of the module and bridging the current lesson to the next.

## 6. Metaphor Guidelines (比喻守则)
*   **Constraint**: Use metaphors only when they reduce cognitive load, not when they add ambiguity.
*   **Central Metaphor**: **The Workbench (工作台)**.
    *   Files = Materials.
    *   Terminal = System Control Center.
    *   Env = The specific set of tools on the table.
*   **Avoid**: Over-dramatizing (e.g., "Magic Spells", "Hollywood Scripts"). Keep it grounded in engineering reality.

## 7. Tone & Voice (语言风格守则)
*   **Professional**: We are training engineers, not playing games.
*   **Rigorous**: Definitions must be precise (even if simplified).
*   **Welcoming**: We acknowledge the difficulty but promise a path through it.
*   **Non-Adversarial (非对抗性)**:
    *   **Bad**: "夺回主权" (Reclaim), "对抗 AI" (Fight AI), "不要被 AI 奴役" (Don't be enslaved).
    *   **Good**: "拥抱主权" (Embrace), "驾驭工具" (Master the tool), "保持觉知" (Maintain awareness).
    *   **Core Logic**: AI is a tool, not an enemy. Sovereignty is about **Responsibility**, not **Warfare**.

---
*Reference this document before writing any M1 content.*
