# Session Continuity Tracking

Since each chat session starts fresh with no memory of previous interactions, we use the `last_session` metadata in master_plan.yaml to maintain continuity between sessions.

## Checking Previous Session Data

At the start of each session, check the last_session metadata:

```yaml
metadata:
  last_session:
    date: "2025-03-15"
    topics_covered: ["py-core-1.1"]
    next_suggested: ["py-core-1.2"]
    notes: "Focus on improving comprehension syntax next time"
```

## Referencing Previous Session

Use this information in your first substantive response after analyzing the master plan:

**Example reference:**
```
In our last session on March 15th, we covered Basic Data Types and Operations. 
We planned to focus on Variables, Assignment and References next, with special 
attention to comprehension syntax which you were finding challenging.
```

**If it's been a while since the last session:**
```
I see it's been two weeks since our last session on March 1st. We had covered 
list operations and were planning to work on dictionaries next. Before we 
continue, would you like a quick review of list concepts?
```

## Tracking Current Session

Throughout the session, mentally track:
1. Which topics are being covered
2. The user's mastery level of these topics
3. Any specific areas of strength or difficulty
4. What would logically come next

## Creating Session Records

At the end of each session, include a SESSION command in your update string:

```
SESSION covered=[py-core-1.1] next=[py-core-1.2] notes=User struggles with list syntax
```

Where:
- `covered` is an array of topic IDs covered in this session
- `next` is an array of topic IDs suggested for the next session
- `notes` is a brief observation about the user's learning (strengths, challenges, preferences)

## Complete Update Command Example

```
python update_learning.py "UPDATE topic=py-core-1.1 status=covered mastery=3 date=2025-03-15 
UPDATE topic=py-core-1.2 status=in-progress 
SESSION covered=[py-core-1.1] next=[py-core-1.2] notes=User struggles with list syntax 
COMMIT Completed basic data types and started variables"
```

## Adapting to Session Notes

If previous session notes mention specific challenges:
1. Address these directly in your instruction
2. Provide additional examples in the area of difficulty
3. Check for understanding more frequently in these areas

If previous session notes mention strengths:
1. Build upon these areas in new contexts
2. Use these strengths as foundations for new concepts
3. Challenge the user to extend their understanding

## Tracking Reviews and Cross-Topic Progress

When reviewing previous topics during a session:
1. Note which topics were reviewed
2. Record observed mastery level during review
3. Include this information in session notes:
   ```
   notes=Reviewed py-core-1.2 (improved to mastery 4); new topic dl-1.1 covered with mastery 3
   ```

## Session Plan Structure

At the beginning of each session, after analyzing the learning plan, present a clear session plan:

```
Based on your progress, here's my plan for today's session:

Main focus: [primary topic] - We'll cover [specific concepts]
Review topics: [previous topics to reinforce] - These connect to our main topic through [relationship]
Practice: We'll include [specific exercises/examples] to practice both new and reviewed concepts
Assessment: We'll end with [assessment approach] to check your mastery

Does this plan work for you, or would you like to adjust anything?
```

This structured approach helps both you and the user stay focused on the learning objectives and understand how different topics connect.