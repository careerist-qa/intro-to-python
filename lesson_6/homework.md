# Homework: Lists

🔥 **Read carefully until the end before you start solving the exercises.** 🔥

## Practice the Basics 💪🏻

### Empty, Pre-populated, and Lists within Lists

Create three lists:

- List #1: Create an empty list and then use append() to populate it with the names of three of your friends.
- List #2: Create the same list, but use the syntax to create it pre-populated.
- List #3: Create the same list, but each element should be a list, where the first sub-element is the friend's name and 
the second sub-element is their age.

```python
# List 1:
list_1 = []
list_1.a???('Friend1')
list_1.???('Friend2')
list_1.???('Friend3')

# List 2:
list_2 = [???, ???, ???]

# List 3:
list_3 = [
    ???,
    ???,
    ???,
]
```

### Retrieve elements from a List

Create print statements to retrieve the following elements from the previous lists:

- From List 2: Retrieve the name of the second friend.
- From List 3: Retrieve the age of the last friend you put in the list.

```python
# Name of second friend
second_friend_name = list_2[???]

# Age of the last friend of the list
last_friend_age = list_3[???][???]
```

### Remove elements from a List

From the lists provided, remove the requested elements. Easy peazy.

```python
cities = ["Houston", "Dallas", "Austin"]
fruits = ["apple", "banana", "orange"]

# Remove Austin from cities without using its index
cities.remove(???)

# Remove the last element from fruits using negative indexes
??? fruits[???]
```

### Verify if an element exists in a list

Given the provided list, write code that prints `YES` if the list contains the word `cheese`

```python
# The list
pantry = ["ham", "bread", "cheese"]

# Write code that prints YES if the list contains "cheese".

if ??? in ???:
    print('YES')
```
### Sorting and Reversing

Given the provided list, write code that sorts and reverses it, as required.

```python
numbers = [6, 34, 17, 9, 2, 11, 57, 9, 32]

# Write code that sorts the list in ascending order without disturbing the original.
sorted_numbers = ???(numbers)

# Write code that reverses (flips) the list without disturbing the original.
# Remember that in this case, casting is required.
reversed_numbers = ???(???(numbers))

# Write code that sorts the list in place, modifying the original.
numbers.s???()

# Write code that reverses (flips) the list in place, modifying the original.
numbers.r???()
```

### Stitching and Slicing

You are given two lists with names of days of the week:

- `work_days` contains the work week days (Mon-Fri) 
- `rest_days` contains the weekend days (Sat-Sun)

Create a third list that contains the _concatenation_ of the previous two. 
Call it `full_week`

Now, write python code that prints a slice from `full_week` with the work days.

```python
work_days = ['mon', 'tue',  'wed', 'thu', 'fri']
rest_days = ['sat', 'sun']

# Concatenate work_days and rest_rays
full_week = ???

# Slice with the work days
print(full_week[???])
```

### Aggregators and Helpers

Given a list of numbers, use helpers and aggregators to answer the questions:

- What's the lowest number?
- What's the highest number?
- What's the sum of all the numbers in the list?
- How many times is the number 9 in the list?
- How many total elements are in the list?

```python
numbers = [6, 34, 17, 9, 2, 11, 57, 9, 32]

# Lowest number
print(???(numbers))

# Highest number
print(???(numbers))

# Sum of everything
print(???(numbers))

# Count number 9s
print(numbers.???(???))

# Total number of elements
print(???(numbers))
```

## Exercises 🏋🏻

### The Biography Creator

Create a program that will ask you for the following items and stores them in a list for later usage:

- Your Name
- Your Age
- The name of the city where you were born

The program should use a variable with a string that will be used as a template. This template should be a sentence 
that can be used to build the person's biography.

Fox example:

`biography = "My name is <NAME>, I'm <AGE> years old and I was born in <CITY>."`
        
Tips: 
- Use f-strings with placeholders to build the actual template, with elements of the list as values.
- Use input() to gather the data.
- Use print() at the end, to show the user's biography.

```python
# Declare an empty list
user_data = []

# Gather user input
name = input("Name: ")
age = input("Age: ")
city = input("City: ")

# Add user input to the list
user_data.???(name)
user_data.???(age)
user_data.???(city)

# Declare your template. Use list elements as values.
biography = f"???"

# Show the user's biography
print(biography)
```

### The Card Deck ♦️♥️♠️♣️

You will be provided with a couple lists that contain the cards for a card deck. One of the lists contains the numbers, 
and the other one contains the faces. 

You will be asked to fill in the blanks to print out certain cards for a card game you've been working on.

🔥 **Tip: You might want to stitch them together first.**

```python
# Here are the card decks.
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
faces = ['J', 'Q', 'K']

# Concatenate them first.
card_deck = ???

# Print out the numbers 1 to 6.
print(card_deck[???])

# Print out the last 3. Do it using POSITIVE indexes.
print(card_deck[???])

# Print out the last 3 (same as before), but using NEGATIVE indexes.
print(card_deck[???])

# Print out everything EXCEPT the first and last.
print(card_deck[???])

# What would you use so the printout includes the following:
# Hint: It's every third card of the full deck.
# ['1', '4', '7', '10', 'K']
print(card_deck[???])

# Print out the EVEN numbers. No faces.
print(???)
```

### The Steps Tracker 👟

Walking is a great way to improve one's health, and it can be fun! Doctors recommend 10,000 steps per day! You would 
like to know how many steps are YOU taking per day and per week.

Write a program that will ask you the number of steps taken each day of the week, for one week. The program should put
the step counts in a list, where index 0 is the number for Monday, index 1 is the number for Tuesday, and so on.
 
Once you have all the steps counts, answer the following questions:
- How many steps you took on Wednesday?
- How many steps you took on the work days (Mon - Fri)?
- How many steps total did you take over the whole week?
- What was the least number of steps you took on a day?
- What was the most number of steps you took on a day? 

```python
monday = input('Steps for Monday: ')
tuesday = input('Steps for Tuesday: ')
wednesday = input('Steps for Wednesday: ')
thursday = input('Steps for Thursday: ')
friday = input('Steps for Friday: ')
saturday = input('Steps for Saturday: ')
sunday = input('Steps for Sunday: ')

steps = [???]

# Steps on Wednesday
print(steps[???])

# Steps on the work days
work_days_steps = steps[???]
print(???(work_days_steps))

# Steps over the whole week
print(???(steps))

# Least number of steps
print(???(steps))

# Highest number of steps
print(???(steps))
```

### Bonus Round: The Speech Reverser and Counter 🎤

Python has a handy little method that allows you to split a string. In its most basic form it splits a string into a
list using the spaces as separators:

Example:
```python
phrase = "My Name is Joseph"
words = phrase.split()
print(words) -> ['My', 'Name', 'is', 'Joseph']
```

More information about split: https://www.w3schools.com/python/ref_string_split.asp

Now, armed with `split()` write a program that does the following:

- Takes a string input from the user.
- Splits it into words.
- Prints out the string with the words in reverse order.
- Prints out the word count. 

```python
# Get input from the user
user_input = ???('Give me a phrase')

# Split user input into words
words = user_input.???()

# Reverse the list and print it
reversed_words = ???(???(words))
print(reversed_words)

# Print the length of the words list
print(???(words))
```