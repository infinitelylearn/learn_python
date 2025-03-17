# Spaced Repetition Implementation

## Review Schedule Based on Mastery

| Mastery Level | Review Frequency | Integration Level |
|---------------|------------------|-------------------|
| 1-2           | 1-2 sessions     | Heavy review      |
| 3             | 3-5 sessions     | Medium review     |
| 4             | 7-10 sessions    | Light review      |
| 5             | 10-15 sessions   | Brief mention     |

## Review Integration Methods

### Light Review (for high mastery topics)
- Brief mention in related examples
- Quick recall questions
- Reference in new material context

### Medium Review (for moderate mastery topics)
- Dedicated examples connecting to new material
- Short practice exercises
- Explicit connections between previous and new concepts

### Heavy Review (for low mastery topics)
- Substantial practice before new content
- Reteaching key concepts
- Multiple exercises reinforcing fundamentals

## Calculating Review Priority

1. Calculate sessions elapsed since last_practiced
2. Compare to recommended review frequency
3. Calculate priority score: 
   ```
   priority = (sessions_elapsed / recommended_frequency) * (6 - mastery_level)
   ```
4. Prioritize topics with highest scores

## Integration with Session Planning

When planning each session:
1. Identify main topic based on progression
2. Calculate review priorities for all previously covered topics
3. Select 1-3 topics for review based on:
   - Priority score from algorithm above
   - Relevance to current topic
   - Available session time

## Tracking Review Effectiveness

After reviewing a topic:
1. Reassess mastery based on demonstrated knowledge
2. Update last_practiced date
3. Note any changes in session update command
4. Record review effectiveness for future reference

## Example Review Scenarios

### Scenario 1: New Topic with Low-Mastery Review
When covering "Pandas for Financial Data" while user has low mastery in "NumPy Arrays":
```
"Today we'll focus on Pandas DataFrames, but I've noticed you might benefit from reinforcing NumPy array concepts, which are foundational for Pandas. We'll start with a brief review of broadcasting and indexing in NumPy before connecting these concepts to Pandas."
```

### Scenario 2: New Topic with High-Mastery Review
When covering "Deep Learning" while user has high mastery in "Python Data Structures":
```
"We'll be exploring neural networks today. As we implement them, we'll make use of your strong knowledge of Python data structures, particularly how lists and dictionaries can represent weights and network architectures."
```
