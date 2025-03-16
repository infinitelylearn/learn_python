# AI-Assisted Learning Framework

An intelligent learning system that uses AI assistants (like Claude) to deliver personalized, spaced-repetition learning with automated progress tracking.

## Overview

This framework provides a structured approach to learning Python and algorithmic trading concepts with an AI tutor. It features:

- **Modular Curriculum**: Organized by topics and subtopics with prerequisites
- **Progress Tracking**: Automated YAML updates via Git
- **Spaced Repetition**: Smart scheduling of review topics
- **Mastery-Based Learning**: Track your mastery level (1-5) for each topic
- **Token-Optimized Design**: Load only necessary instructions when needed
- **Project-Based Learning**: Apply concepts through practical projects
- **Personalized Learning**: Adapt to your learning style and preferences

## Getting Started

### Prerequisites

- GitHub account (private or public repository)
- Python 3.7+ with PyYAML installed (`pip install pyyaml`)
- AI assistant access (Claude recommended)

### Setup Instructions

1. **Clone this template repository**

```bash
git clone https://github.com/your-username/learning-framework.git
cd learning-framework
```

2. **Install dependencies**

```bash
# Create a conda environment (recommended)
conda create -n learning_framework python=3.10
conda activate learning_framework

# Install required packages
conda install pyyaml
```

3. **Customize your master plan**

Edit `master_plan.yaml` to set your learning preferences:

```yaml
metadata:
  learning_preferences:
    style: "code-first"  # or "visual", "theoretical", "project-based"
    session_length: "medium"  # "short", "medium", "long"
    feedback_type: "detailed"  # "brief", "detailed", "challenging" 
    example_domain: "forex"  # "stocks", "forex", "crypto", "options"
    other: ""  # any additional preferences
```

## File Structure

```
learning-framework/
├── master_plan.yaml                    # Master tracking file
├── update_learning.py                  # Update script
├── prompts_instructions/               # Prompts and instruction files
│   ├── framework_prompt.md             # Core Claude prompt
│   ├── instruction_learning_styles.md  # Specialized instruction files
│   ├── instruction_projects.md
│   ├── instruction_financial_examples.md
│   ├── instruction_session_tracking.md
│   └── instruction_update_commands.md
├── module_core_python.yaml             # Learning modules
├── module_data_handling.yaml
├── module_performance.yaml
├── module_finance.yaml
├── module_machine_learning.yaml
├── module_deep_learning.yaml
├── module_reinforcement_learning.yaml
├── module_advanced_topics.yaml
├── module_production.yaml
└── module_projects.yaml
```

## How to Use

### Starting a New Session

1. **Open your AI assistant chat** (Claude recommended)
2. **Copy the entire contents of `prompts_instructions/framework_prompt.md`** and paste it as Claude's custom instructions
3. **Start a new conversation with a simple message** like "Let's continue my Python learning"
4. **Let Claude guide the session**:
   - Claude will request `master_plan.yaml`
   - Upload the file when prompted
   - Claude will analyze your progress and recommend topics
   - Claude will request additional files as needed

### During the Session

Claude will:
1. Recommend the next logical topic based on your progress
2. Adapt to your learning preferences
3. Provide examples in your preferred financial domain
4. Track your progress throughout the session
5. Release files when no longer needed to save tokens

### Ending the Session

At the end of each session, Claude will:
1. Provide an update command to track your progress
2. Recommend what to study next
3. Give you a string to run like:

```bash
python update_learning.py "UPDATE topic=py-core-1.1 status=covered mastery=3 UPDATE topic=py-core-1.2 status=in-progress SESSION covered=[py-core-1.1] next=[py-core-1.2] notes=User shows strong understanding COMMIT Completed basic data types"
```

Run this command to:
- Update your progress files
- Record session information
- Commit and push changes to GitHub

## Customization

### Adapting to Other Domains

To use this framework for a different subject:

1. Modify the module YAML files with your own topics
2. Update the financial examples to match your domain
3. Adjust the learning preferences to reflect your field
4. Modify project milestones to match your goals

### Adding New Topics

To add new topics:

1. Add entries to the appropriate module YAML file
2. Set prerequisites, priority, and other metadata
3. Create subtopics with logical progression
4. Link to other topics as needed

## Troubleshooting

### Common Issues

1. **Git Authentication Issues**:
   - Use `--no-push` flag to skip pushing: `python update_learning.py "..." --no-push`
   - Set up SSH keys or credential manager for seamless authentication

2. **Claude Not Following the Framework**:
   - Ensure you've copied the ENTIRE framework prompt at the start
   - Make sure Claude can access all necessary files

3. **YAML Parsing Errors**:
   - Check for proper indentation in your YAML files
   - Use the `--backup` flag to create backups before updating: `python update_learning.py "..." --backup`

## Advanced Features

### Command Line Options

The update script supports several flags:

```bash
python update_learning.py "UPDATE..." [options]

Options:
  --backup       Create backups before updating
  --no-push      Skip pushing to GitHub
  --verbose      Show detailed output
```

### Learning Preferences

Adjust your learning style at any time with the PREF command:

```bash
python update_learning.py "PREF style=visual domain=forex COMMIT Updated learning preferences"
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This framework uses AI assistants like Claude to deliver personalized learning
- Inspired by spaced repetition systems and mastery-based learning approaches