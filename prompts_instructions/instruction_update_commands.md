# Update Command Formatting

After completing a session, provide a single command that updates all necessary files. This command uses the `update_learning.py` script to update YAML files, track session information, and commit changes to GitHub.

## Command Structure

The complete command follows this format:

```
python update_learning.py "UPDATE topic=ID1 param=value param=value 
UPDATE topic=ID2 param=value 
SESSION covered=[topic1,topic2] next=[topic3] notes=Brief observation 
PREF style=value domain=value 
COMMIT Descriptive message about the session"
```

## Command Components

### UPDATE Command

Use `UPDATE` to modify topic or subtopic status and mastery:

```
UPDATE topic=py-core-1.1 status=covered mastery=3 date=2025-03-15
```

Parameters:
- `topic`: The ID of the topic or subtopic to update (required)
- `status`: Current progress - "uncovered", "in-progress", or "covered"
- `mastery`: Integer value from 1-5 representing mastery level
- `date`: The date of the session (added automatically if not specified)

### SESSION Command

Use `SESSION` to track continuity between sessions:

```
SESSION covered=[py-core-1.1,py-core-1.2] next=[py-core-1.3] notes=User excelled at string operations
```

Parameters:
- `covered`: List of topic IDs covered in this session
- `next`: List of topic IDs suggested for next session
- `notes`: Brief observation about learning progress

### PREF Command

Use `PREF` to update learning preferences:

```
PREF style=visual session_length=medium feedback_type=detailed domain=forex
```

Parameters:
- `style`: Learning style - "code-first", "visual", "theoretical", "project-based"
- `session_length`: Preferred session length - "short", "medium", "long"
- `feedback_type`: Preferred feedback - "brief", "detailed", "challenging"
- `domain`: Example domain - "forex", "stocks", "crypto", "options"
- `other`: Any additional preference notes

### COMMIT Command

End with `COMMIT` followed by a descriptive message:

```
COMMIT Completed basic data types and started variables
```

The commit message should concisely describe what was accomplished in the session.

## Examples

### Basic Topic Update

```
python update_learning.py "UPDATE topic=py-core-1.1 status=covered mastery=3 COMMIT Completed basic data types"
```

### Multiple Updates with Session Tracking

```
python update_learning.py "UPDATE topic=py-core-1.1 status=covered mastery=3 
UPDATE topic=py-core-1 mastery=2 
UPDATE topic=py-core-1.2 status=in-progress 
SESSION covered=[py-core-1.1] next=[py-core-1.2] notes=User grasps concepts quickly but needs more practice with list syntax 
COMMIT Completed basic data types and started variables"
```

### Updating Preferences

```
python update_learning.py "UPDATE topic=data-1.1 status=covered mastery=4 
PREF style=visual domain=forex 
COMMIT Completed NumPy arrays; updated learning preferences to visual style"
```

### Project Milestone Update

```
python update_learning.py "UPDATE topic=project-1.1 status=covered mastery=3 
UPDATE topic=project-1 status=in-progress 
SESSION covered=[project-1.1] next=[project-1.2] notes=Good progress on API integration
COMMIT Completed first project milestone: Data Collection API"
```

## Command Formatting Guidelines

1. Always start with `python update_learning.py` followed by the command string in quotes
2. Chain multiple updates together for all affected topics and subtopics
3. Include topic mastery and status changes
4. Add SESSION tracking for continuity
5. Update PREF when learning preferences change
6. End with a COMMIT message describing the session

Present this command clearly at the end of each session, formatted in a code block for easy copying.
