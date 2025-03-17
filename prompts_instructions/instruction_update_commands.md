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

## Cross-Topic Mastery Updates

When a session demonstrates evidence of changed mastery in previously covered topics:

1. Include those topics in your UPDATE commands
2. Adjust mastery scores based on demonstrated ability:
   ```
   UPDATE topic=py-core-1.4 status=covered mastery=3 date=2025-03-17 
   UPDATE topic=py-core-1.2 mastery=4  # Increased from 3 based on demonstrated skills
   ```
3. Guidelines for mastery changes:
   - Increase mastery (e.g., 3→4) when the user demonstrates skills beyond their previous level
   - Decrease mastery (e.g., 4→3) when the user shows significant gaps in previously "mastered" topics
   - Include explicit reasoning in SESSION notes: `notes=Improved mastery of variables (py-core-1.2) observed in function parameter handling`

4. Example of multi-topic update:
   ```
   python update_learning.py "UPDATE topic=data-2.2 status=covered mastery=3 date=2025-03-15
   UPDATE topic=py-core-2.3 mastery=4  # Improved comprehension skills observed
   UPDATE topic=data-1.2 mastery=2  # Struggling with broadcasting concepts
   SESSION covered=[data-2.2] next=[data-2.3] notes=Strong with time series concepts, needs review of NumPy broadcasting
   COMMIT Covered Time Series Analysis; adjusted previous topic mastery"
   ```

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

### Review and Cross-Topic Update

```
python update_learning.py "UPDATE topic=dl-1.1 status=covered mastery=3 
UPDATE topic=py-core-2.1 mastery=4  # Previously mastery 3, improved during list operations in neural net implementation
SESSION covered=[dl-1.1] next=[dl-1.2] notes=Neural network basics covered; list manipulation skills showed improvement during implementation
COMMIT Completed Neural Network Fundamentals and observed improved Python data structure skills"
```

## Command Formatting Guidelines

1. Always start with `python update_learning.py` followed by the command string in quotes
2. Chain multiple updates together for all affected topics and subtopics
3. Include topic mastery and status changes
4. Add SESSION tracking for continuity
5. Update PREF when learning preferences change
6. End with a COMMIT message describing the session

Present this command clearly at the end of each session, formatted in a code block for easy copying.