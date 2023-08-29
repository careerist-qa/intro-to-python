### Empty, Pre-populated, and Lists within Lists

```python
# List 1: Create an empty list and populate it with elements.
list_1 = []
list_1.append('Friend1')
list_1.append('Friend2')
list_1.append('Friend3')

# List 2: Create a pre-populated list.
list_2 = ['Friend1', 'Friend2', 'Friend3']

# List 3: Create a list in which each element is a list with name and age.
list_3 = [
    ['Friend1', 30],
    ['Friend2', 32],
    ['Friend3', 34],
]
```

### Retrieve elements from a List
References the lists from the exercise above.
```python
# Name of second friend
second_friend_name = list_2[1]

# Age of the last friend of the list
last_friend_age = list_3[-1][1]
```

### Remove elements from a List
```python
cities = ["Houston", "Dallas", "Austin"]
fruits = ["apple", "banana", "orange"]

# Remove Austin from cities without using its index
cities.remove("Austin")

# Remove the last element from fruits using negative indexes
del fruits[-1]
```

### Verify if an element exists in a list
```python
# The list
pantry = ["ham", "bread", "cheese"]

# Write code that prints YES if the list contains "cheese".
if "cheese" in pantry:
    print('YES')
```
### Sorting and Reversing
```python
numbers = [6, 34, 17, 9, 2, 11, 57, 9, 32]

# Write code that sorts the list in ascending order without disturbing the original.
sorted_numbers = sorted(numbers)

# Write code that reverses (flips) the list without disturbing the original.
# Remember that in this case, casting is required.
reversed_numbers = list(reversed(numbers))

# Write code that sorts the list in place, modifying the original.
numbers.sort()

# Write code that reverses (flips) the list in place, modifying the original.
numbers.reverse()
```

### Stitching and Slicing
```python
work_days = ['mon', 'tue',  'wed', 'thu', 'fri']
rest_days = ['sat', 'sun']

# Concatenate work_days and rest_rays
full_week = ???

# Slice with the work days
print(full_week[???])
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
### The Biography Creator
```python
# Declare an empty list
user_data = []

# Gather user input
name = input("Name: ")
age = input("Age: ")
city = input("City: ")

# Add user input to the list
user_data.append(name)
user_data.append(age)
user_data.append(city)

# Declare your template. Use list elements as values.
biography = f"My name is {name}, I'm {age} years old and I was born in {city}."

# Show the user's biography
print(biography)
```
### The Card Deck
```python
# Here are the card decks.
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
faces = ['J', 'Q', 'K']

# Concatenate them first.
card_deck = numbers + faces

# Print out the numbers 1 to 6.
print(card_deck[0:6])

# Print out the last 3. Do it using POSITIVE indexes.
print(card_deck[10:13])

# Do the same, but using NEGATIVE indexes.
print(card_deck[-3:])

# Print out everything EXCEPT the first and last.
print(card_deck[1:-1])

# What would you use so the printout includes the following:
# Hint: It's every third card of the full deck.
# ['1', '4', '7', '10', 'K']
print(card_deck[::3])

# Print out the EVEN numbers. No faces.
print(numbers[1::2])
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