## Overview
This project implements an automated, multi-agent workflow for transforming a raw content idea into a fully-developed content strategy with validated outputs, timelines, milestones, and KPIs.

## Workflow Diagram
```mermaid
graph TD
    START((Start)) --> A["User Input: Brief about content idea"]
    A --> B[Brainstorming Agent]
    B --> C{"Interact with User: Ask questions to clarify idea"}
    C --> D["User provides feedback and details"]
    D --> B
    B --> E["Quality Gate 1: Rate the Idea (User Rating 1-10)"]
    E --> F{Rating > 7?}
    F -->|No| G["Reject or Revise Idea"]
    G --> B
    F -->|Yes| H[Deep Research Agent]
    H --> I[Advanced Analysis Agent]
    I --> J["Create 'Big Picture' Strategy"]
    J --> K["Big Picture includes: - Content Type - Publishing Plan - Target Audience - Channels"]
    K --> L["Quality Gate 2: User rates Big Picture (Rating 1-10)"]
    L --> M{Rating > 7?}
    M -->|No| N["Revise Strategy"]
    N --> J
    M -->|Yes| O[Final Output Agent]
    O --> P["Output Includes: Final Content Timeline with Start/End dates Milestones KPIs"]
    P --> END((End))
```

## Agents & Components
Agent	             Responsibility
Brainstorming Agent	 Clarifies the initial idea through interactive Q&A with the user
Deep Research Agent	 Conducts background research on the validated idea
Advanced Analysis    Agent	Analyzes research findings to inform strategy
Final Output Agent	 Generates final deliverables (content, timeline, milestones, KPIs)

## Quality Gates
Gate 1 (Idea Rating): User rates the clarified idea on a scale of 1–10.

Pass: > 7 → Proceed to research

Fail: ≤ 7 → Revise and re-enter brainstorming

Gate 2 (Strategy Rating): User rates the "Big Picture" strategy on a scale of 1–10.

Pass: > 7 → Proceed to final output

Fail: ≤ 7 → Revise strategy and re-evaluate

##Inputs
Brief description of a content idea (from user)

##Outputs
✅ Final content piece

📅 Timeline with start and end dates

🎯 Milestones

📊 KPIs for measuring success


### How to Use (Conceptual)
Submit a short content idea.

Answer clarifying questions from the Brainstorming Agent.

Rate the refined idea (must be >7/10 to continue).

The system researches and analyzes automatically.

Review the "Big Picture" strategy and rate it (>7/10 to continue).

Receive final content plan with timeline, milestones, and KPIs.
