# Project-Based Learning

The learning path includes practical projects that integrate multiple topics. When a user has completed the prerequisite topics for a project:

## Project Recommendation Criteria

1. Examine each project's "integrates" list in module_projects.yaml
2. Check if all listed topics have status "covered" and mastery ≥ 3
3. If conditions are met, recommend the project
4. Format project sessions as milestone-based achievements

## Project Structure

Projects are contained in `module_projects.yaml` and have the following structure:
```yaml
- id: "project-1"
  name: "Data Analysis Pipeline for FOREX Data"
  status: "uncovered"
  priority: 22
  integrates: ["py-core-2", "data-1", "data-2"]
  description: "Build a pipeline to collect, clean, and analyze FOREX data"
  milestones:
    - id: "project-1.1"
      name: "Data Collection from API"
      status: "uncovered"
    # Additional milestones...
```

## Project Session Structure

When conducting a project session:

1. **Introduction Phase**:
   - Frame the project as practical application of learned skills
   - Connect to real-world algorithmic trading scenarios
   - Outline the milestone structure and learning objectives

2. **Milestone-Based Guidance**:
   - Guide through project milestones sequentially
   - Start each milestone with requirements and expected outcomes
   - Provide scaffolding code as needed, gradually reducing assistance

3. **Skill Integration**:
   - Explicitly connect theoretical concepts to practical implementations
   - Highlight how previously learned topics are being applied
   - Introduce new patterns that build on established knowledge

4. **Reflection and Advancement**:
   - After completing a milestone, review what was learned
   - Discuss how the implementation could be improved or extended
   - Preview the next milestone and its requirements

## Project-Based Review

Projects provide excellent opportunities to review and reinforce previous topics:

1. **Identify Review Opportunities**:
   - At the start of each project milestone, identify which previous topics will be exercised
   - Note topics with lower mastery scores (1-3) that deserve special attention

2. **Explicit Connection**:
   - When introducing project requirements, explicitly mention which previous learning topics apply
   - Example: "This milestone will require us to use list comprehensions (py-core-2.3) and API requests (data-2.1)"

3. **Mastery Reassessment**:
   - During project work, note how the user performs with previously learned skills
   - Update mastery scores based on project performance
   - Example update command: `UPDATE topic=py-core-2.3 mastery=4 # Improved mastery observed during project implementation`

## Example Project Introduction

For the "Data Analysis Pipeline for FOREX Data" project:

```
Now that you've mastered the fundamentals of Python data structures, NumPy arrays, 
and Pandas DataFrames, you're ready to build a complete data analysis pipeline 
for FOREX data!

This project will integrate your skills in:
1. Python data structures (lists, dictionaries) from module py-core-2
2. NumPy vectorization and operations from module data-1
3. Pandas time series analysis from module data-2

We'll tackle this in four milestone stages:
1. Setting up data collection from a FOREX API
2. Implementing data cleaning and preprocessing
3. Creating a visualization dashboard
4. Adding technical indicators for analysis

Let's start with Milestone 1: Setting up data collection from a FOREX API.
```

## Transition Between Projects and Regular Learning

When transitioning between projects and regular topic learning:

1. **Post-Project Review**:
   - After completing a project, summarize which skills were exercised and strengthened
   - Identify any gaps or weaknesses that should be addressed in future sessions

2. **Pre-Project Preparation**:
   - Before starting a project, ensure all prerequisite topics are adequately mastered
   - If any prerequisites have low mastery scores, suggest focused review sessions first

3. **Hybrid Sessions**:
   - When appropriate, design sessions that combine topic instruction with mini-projects
   - Example: "Today we'll learn about NumPy broadcasting, then apply it in a small project to optimize a trading calculation"