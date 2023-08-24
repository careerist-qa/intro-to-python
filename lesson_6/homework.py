# READ CAREFULLY TO THE END BEFORE YOU START SOLVING THE EXERCISES.

# Homework Lesson 6: Lists
# Please use concepts and tools you've learned in previous lessons whenever you can.

# EXAMPLE EXERCISE
# We solved this one for you, to give you an idea of what we expect you to do.

# ----------------------------------------------------------------------------------------------------------------------

"""
Exercise 0: The Lottery

You have the following team members at work: Eric, Tom, Kelly and You.
Your company wants to do a lottery, in such a way that those born on an EVEN (divisible by 2) number year receive a
prize.

Create a little program that will ask for the birth years of you and your teammates and builds a list of those
that will receive a prize. Print the result at the end.
"""

# Create an empty list.
prize_receivers = []

# Take the year input and cast it as int, so we can perform a modulus calculation on it later.
birth_year_eric = int(input("Eric's birth year:"))
birth_year_tom = int(input("Tom's birth year:"))
birth_year_kelly = int(input("Kelly's birth year:"))
birth_year_you = int(input("Your birth year:"))

# Figure out if any of the years are multiples of two, by using the modulus operator (%).
# Those that are, are added to the prize_receivers list.
if birth_year_eric % 2 == 0:
    prize_receivers.append("Eric")

if birth_year_tom % 2 == 0:
    prize_receivers.append("Tom")

if birth_year_kelly % 2 == 0:
    prize_receivers.append("Kelly")

if birth_year_you % 2 == 0:
    prize_receivers.append("You")

# Print the result.
print("The following people receive a prize:")
print(prize_receivers)

# ----------------------------------------------------------------------------------------------------------------------
"""
Exercise 1: The Biography Creator

Create a program that will ask you for the following items and stores them in a list for later usage:
- Your Name
- Your Age
- The name of the city where you were born

The program should use a variable with a string that will be used as a template. This template should be a sentence 
that can be used to build the person's biography.

Fox example:
        biography = "My name is <NAME>, I'm <AGE> years old and I was born in <CITY>."
        
Tips: 
- Use f-strings with placeholders to build the actual template, with elements of the list as values.
- Use input() to gather the data.
- Use print() at the end, to show the user's biography.
"""
# Declare an empty list
user_data = []

# Add user input to the list
user_data.???(???("What is your name?"))
user_data.???(???)
user_data.???(???)

# Declare your template. Use list elements as values.
biography = f"???"

# Show the user's biography
print(biography)

"""
Exercise 2: The Card Deck

You will be provided with a couple lists that contain the cards for a card deck. One of the lists contains the numbers, 
and the other one contains the faces. 

You will be asked to fill-in the blanks to print out certain cards for a card game you've been working on.

Tip: You might want to stitch them together first.
"""

# Here are the card decks.
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
faces = ['J', 'Q', 'K']

# You might want to stitch them together first.
card_deck = ???

# Print out the numbers 1 to 6.
print(card_deck[???])

# Print out the last 3. Do it using positive indexes AND negative indexes.
print(card_deck[???])
print(card_deck[???])

# Print out everything EXCEPT the first and last.
print(card_deck[???])

# What would you use so the printout includes the following:
# Hint: It's every third card of the full deck.
# ['1', '4', '7', '10', 'K']
print(card_deck[???])

# Print out the EVEN numbers. No faces.
print(???)

# Print out the FACES only, in descending order, without affecting the original lists.
# Hint: You can slice -> reverse -> print
???
???
print(???)

"""
Exercise 3: The Steps Tracker

Walking is a great one to improve one's health, and it can be fun! Doctors recommend 10,000 steps per day! You would 
like to know how many steps are YOU taking per day and per week.

Write a program that will ask you the number of steps taken each day of the week, for one week. The program should put
the step counts in a list, where index 0 is the number for Monday, index 1 is the number for Tuesday, and so on.
 
Once you have all the steps counts, answer the following questions:
- How many steps you took on Wednesday?
- How many steps you took on the work days (Mon - Fri)?
- How many steps you took on the weekend (Sat - Sun)?
- How many steps total did you take over the whole week?
- What was the least number of steps you took on a day?
- What was the most number of steps you took on a day? 
"""

# No hints for this one!

"""
Exercise 4: The Speech Reverser and Counter

Python has a handy little method that allows you to split a string. In its most basic form it splits a string into a
list using the spaces as separators:

Example: 
    phrase = "My Name is Joseph"
    words = phrase.split()
    
    print(words) -> ['My', 'Name', 'is', 'Joseph']

More information about split: https://www.w3schools.com/python/ref_string_split.asp

Now, armed with split(), write a program that does the following:

- Takes a string input from the user.
- Splits it into words.
- Prints out the string with the words in reverse order.
- Prints out the word count. 
"""

# No hints for this one!

"""
Exercise 5: Figure out what this does!

Analyze the following code, adding notes and comments of what do you think every step does. 
Some pieces will look unfamiliar to you. For those pieces, just take a best guess about what do you think they do.

Googling and reviewing documentation is perfectly okay!
"""

recipe = [
    ['Flour', '500gr'],
    ['Milk', '200ml'],
    ['Egg', '1pc'],
    ['Sugar', '2tbsp'],
]

pantry = ["Flour", "Egg", "Sugar"]

for ingredient in recipe:
    if ingredient[0] not in pantry:
        print(f"You need to buy {ingredient[1]} of {ingredient[0]}!")
