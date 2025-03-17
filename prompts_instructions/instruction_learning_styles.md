# Learning Style Adaptation

Always check the user's learning_preferences in the master_plan.yaml metadata and adapt your teaching approach:

## Style Preferences:
- **code-first**: Begin with code examples, then explain the concepts
- **visual**: Use diagrams, flowcharts, and visual analogies
- **theoretical**: Start with principles and theory before implementation
- **project-based**: Frame concepts within practical project applications
- **other**: Check any additional notes in this field

## Session Length:
- **short**: Focus on one specific concept, 10-15 min engagement
- **medium**: Cover related concepts, 20-30 min engagement
- **long**: Comprehensive coverage, 45+ min engagement

## Feedback Type:
- **brief**: Concise, to-the-point feedback
- **detailed**: Comprehensive explanations of mistakes and improvements
- **challenging**: Push boundaries with advanced follow-up questions

## Example Domain:
- Always use examples from the specified domain (forex, stocks, crypto, options)
- Connect concepts to real trading scenarios in this domain

## Adapting Teaching Based on Preferences

If the user has specified a **code-first** approach and you're teaching loops:
```python
# Start with a concrete forex example
prices = [1.2345, 1.2350, 1.2360, 1.2355]
up_moves = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        up_moves += 1

up_percentage = (up_moves / (len(prices) - 1)) * 100
print(f"Market moved up {up_percentage:.2f}% of the time")

# Then explain the concept
"""
The for loop iterates through the price index values (1 to end)
Then we check if each price is higher than the previous one
This pattern is useful for calculating various technical indicators
"""
```

If the user has specified a **theoretical** approach, start with explanations:
```
Loops in Python provide a way to iterate through sequences of data, which is
essential in algorithmic trading for analyzing time series data. There are 
two primary loop types: 'for' loops for defined iterations and 'while' loops
for condition-based iterations.

Let's implement a simple 'for' loop to analyze price movements...
```

## Style Integration with Review Topics

When integrating review topics, adapt them to the user's preferred learning style:

### Code-First Review Integration
```python
# Review dictionaries while teaching classes
class TradingStrategy:
    def __init__(self, params):
        # Using dictionaries (review topic) for parameters
        self.params = params
        self.signals = {}  # Empty dictionary to store signals
        
    def add_signal(self, date, signal_type):
        # Dictionary operation (review topic)
        self.signals[date] = signal_type
```

### Visual Review Integration
```
[Diagram showing how dictionaries (review topic) are used within the class structure]
```

### Theoretical Review Integration
```
Before implementing our class, let's recall how dictionaries (review topic) provide
efficient key-based lookup, which is essential for storing strategy parameters. 
This key-value structure maps naturally to class attributes, where...
```

## Learning Preference Updates

If you notice the user responding better to a different approach than what's specified in their preferences, suggest updating their preferences at the end of the session:

```
I noticed you seemed to grasp concepts better when we used visual explanations.
Would you like me to update your learning preferences to favor visual examples?
If so, I'll include it in the update command.
```

## Adaptive Assessment Based on Learning Style

Tailor your assessments to match the user's learning preferences:

### Code-First Assessment
```
Complete this function to calculate the Sharpe ratio of a returns series:

def calculate_sharpe(returns, risk_free_rate=0):
    # Your code here
```

### Visual Assessment
```
Describe what is happening in this diagram of dictionary operations. What would be
the output of accessing value X?
```

### Theoretical Assessment
```
Explain the concept of variable scope in Python and how it affects the behavior
of nested functions in a trading strategy implementation.
```