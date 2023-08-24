
### Sorting and Reversing
```python
numbers = [6, 34, 17, 9, 2, 11, 57, 9, 32]

# Write code that sorts the list in ascending order without disturbing the original.
sorted_numbers = sorted(numbers)

# Write code that reverses (flips) the list without disturbing the original.
# Remember that in this case, some casting is required.
reversed_numbers = list(reversed(numbers))

# Write code that sorts the list in place, modifying the original.
numbers.sort()

# Write code that reverses (flips) the list in place, modifying the original.
numbers.reverse()
```

### Aggregators and Helpers

```python
numbers = [6, 34, 17, 9, 2, 11, 57, 9, 32]

# Lowest number
print(min(numbers))

# Highest number
print(max(numbers))

# Sum of everything
print(sum(numbers))

# Count number 9s
print(numbers.count(9))

# Total elements
print(len(numbers))
```

### Steps Tracker
```python
monday = input('Steps for Monday: ')
tuesday = input('Steps for Tuesday: ')
wednesday = input('Steps for Wednesday: ')
thursday = input('Steps for Thursday: ')
friday = input('Steps for Friday: ')
saturday = input('Steps for Saturday: ')
sunday = input('Steps for Sunday: ')

steps = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

# Steps on Wednesday
print(steps[2])

# Steps on the work days
work_days_steps = steps[0, 5]
print(sum(work_days_steps))

# Steps over the whole week
print(sum(steps))

# Least number of steps
print(min(steps))

# Highest number of steps
print(max(steps))
```

### Bonus Round: The Speech Reverser and Counter
```python
# Get input from the user
user_input = input('Give me a phrase')

# Split user input into words
words = user_input.split()

# Reverse the list and print it
reversed_words = list(reversed(words))
print(reversed_words)

# Print the length of the words list
print(len(words))
```