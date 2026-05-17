# Content Strategy Automation Flow

## Overview
This project implements an automated, multi-agent workflow for transforming a raw content idea into a fully-developed content strategy with validated outputs, timelines, milestones, and KPIs.

## Workflow Diagram
```mermaid
graph TD
    START((Start)) --> A[User Input: Brief about content idea]
    
    A --> B[Brainstorming Agent]
    B --> C{Interact with User:<br/>Ask questions to clarify idea}
    C --> D[User provides feedback & details]
    D --> B
    
    B --> E[Quality Gate 1:<br/>Rate the Idea<br/>(User Rating 1-10)]
    E --> F{Rating > 7?}
    F -->|No| G[Reject / Revise Idea]
    G --> B
    
    F -->|Yes| H[Deep Research Agent]
    H --> I[Advanced Analysis Agent]
    
    I --> J[Create "Big Picture" Strategy]
    J --> K[Big Picture includes:<br/>- Content Type<br/>- Publishing Plan<br/>- Target Audience<br/>- Channels]
    
    K --> L[Quality Gate 2:<br/>User rates Big Picture<br/>(Rating 1-10)]
    L --> M{Rating > 7?}
    M -->|No| N[Revise Strategy]
    N --> J
    
    M -->|Yes| O[Final Output Agent]
    O --> P[Output Includes:<br/>✅ Final Content<br/>📅 Timeline with Start/End dates<br/>🎯 Milestones<br/>📊 KPIs]
    
    P --> END((End))
