# Content Strategy Automation Flow

## Overview
This project implements an automated, multi-agent workflow for transforming a raw content idea into a fully-developed content strategy with validated outputs, timelines, milestones, and KPIs.

graph TD
    START((Start)) --> A["User Input: Brief about content idea"]
    
    A --> B[Brainstorming Agent]
    B --> C{"Interact with User:
    Ask questions to clarify idea"}
    C --> D[User provides feedback and details]
    D --> B
    
    B --> E["Quality Gate 1:
    Rate the Idea
    (User Rating 1-10)"]
    E --> F{Rating > 7?}
    F -->|No| G[Reject or Revise Idea]
    G --> B
    
    F -->|Yes| H[Deep Research Agent]
    H --> I[Advanced Analysis Agent]
    
    I --> J["Create 'Big Picture' Strategy"]
    J --> K["Big Picture includes:
    - Content Type
    - Publishing Plan
    - Target Audience
    - Channels"]
    
    K --> L["Quality Gate 2:
    User rates Big Picture
    (Rating 1-10)"]
    L --> M{Rating > 7?}
    M -->|No| N[Revise Strategy]
    N --> J
    
    M -->|Yes| O[Final Output Agent]
    O --> P["Output Includes:
    ✅ Final Content
    📅 Timeline with Start/End dates
    🎯 Milestones
    📊 KPIs"]
    
    P --> END((End))
