# HOMEWORK: Dictionaries
# Read carefully until the end before you start solving the exercises.

# Basic Dictionary

# Create an empty dictionary and then add a few of your friends. Make the key their email (can be fake)
# and the value their name. When you're done, create the same dictionary as a pre-populated dictionary.

# ----------------------------------------------------------------------------------------------------------------------

# Nested Dictionary

# Create a nested dictionary for a list of 5 company employees.
# The key should be their employee id (an integer from 1-5 will do) and the value should be a dictionary with
# the name, department and salary of the employee.

# ----------------------------------------------------------------------------------------------------------------------

# Accessing Values

# Use the previous nested dictionary and write some print statements that will answer the following:

# - Print a list of the employee IDs
# - Print the employee data for employee with the ID 3.
# - Loop over the employees and print all their names and salaries.

# ----------------------------------------------------------------------------------------------------------------------

# Updating Values

# We have the following dictionary with employee salaries.

salaries = {
    'james' : 10000,
    'tom' : 15000,
    'ryan' : 16000,
    'julia' : 17000
}

# We need to increase everyone's salary by 1,000 and also add a new employee joseph with a salary of 18,000.
# Please come up with a way to do this using update()

# ----------------------------------------------------------------------------------------------------------------------

# Deleting Values

# You remember those employees from Updating Values section? Well, Julia got fired, so we need to remove her
# name from the salaries dictionary. How would you do that?

# ----------------------------------------------------------------------------------------------------------------------

# Iterating over Dictionaries

# Given the list of movies below, please use view objects (keys(), values(), items() - where necessary) to answer
# the questions:

# - Is Black Panther in the list of movies?
# - Is there any movie for the year 2021?
# - Print a message for each element that shows the year, the title and the position in the dictionary (1-5).
#   Hint: use a counter.

films = {
   2016: "Star Wars: Episode VII - The Force Awakens",
   2017: "Star Wars: Episode VIII - The Last Jedi",
   2018: "Black Panther",
   2019: "Avengers: Endgame",
   2020: "Bad Boys for Life"
}

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 1. Animal Shelter Volunteer

# You volunteer in a local animal shelter and you've stored information
# about different pets in a Python dictionary.
# Your task is to create a Python program that helps you:

# - Access the age of specific pets by their names.
# - Find out which pets are not yet adopted.
# - Identify the most common animal type in the shelter (e.g., dog, cat).

# Pre-code
# Initialize the shelter_pets dictionary
# shelter_pets = {
#   'Whiskers': {'Age': 2, 'Type': 'Cat', 'Adopted': False},
#   'Fido': {'Age': 4, 'Type': 'Dog', 'Adopted': True},
#   'Patch': {'Age': 1, 'Type': 'Dog', 'Adopted': False},
#   'Snowball': {'Age': 3, 'Type': 'Rabbit', 'Adopted': True}
# }

# Access and print the age of Whiskers
# print(shelter_pets['Whiskers']['Age'])  # Should output 2

# Access and print if Patch is a dog or cat
# print(???)

# Access and print if Snowball is adopted or not
# print(???)

# Find out which pets are not yet adopted and print their names
# for ???, ??? in shelter_pets.i???():
# if not info['???']:
# print(pet)

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 2. Best - selling books

# Create a Python program to manage a collection of best-selling books
# and their publication years. Your initial list of best-selling books may have inaccuracies
# or could be outdated. Therefore, you'll also practice updating single and multiple entries
# in your dictionary. Specifically, you will:

# - Update the title of a book for a specific year due to a naming convention change.
# - Update the titles for multiple books at once based on new sales data.
# - Delete a book and its year from the collection as it's no longer considered a best-seller.
# - Print the title of the book published in a specific year.

# Pre-code:
# Initialize a dictionary called best_selling_books to store your collection.

# best_selling_books = {
#   1997: "Harry Potter and the Philosopher's Stone",
#   1984: "Neuromancer",
#   2003: "The Kite Runner",
#   2015: "Go Set a Watchman"
# }

# The U.S. title for the Harry Potter book published in 1997 is "Harry Potter and the Sorcerer's Stone".
# Update the title to its U.S. version.
# best_selling_books ???  = "Harry Potter and the Sorcerer's Stone"

# New sales data reveals that "The Hunt for Red October" was the actual best-seller for 1984
# and "The Da Vinci Code"  for 2003.
# Update these in a single operation.

# best_selling_books.u???({
#   1984: ???
#   ???: ???
# ???

# The book published in 2015, "Go Set a Watchman," is no longer considered a best-seller.
# Use the del keyword to remove this entry from the dictionary.

# Print the updated dictionary of best selling books.

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 3. Manage Music Collection
# Create a Python program that manages a collection of music albums and their release years.
# You will use a dictionary where the keys are the release years and the values are the names of albums.
# The program should allow you to:

# - Print all the release years (keys) from the dictionary.
# - Print all the album names (values) from the dictionary.
# - Print both the release years and album names together.
# - Check if a particular year or album exists in the collection.


# Steps and pre-code
# Initialize a dictionary to store Bob Dylan's albums
# dylan_albums = {
#   1962: "Bob Dylan",
#   1963: "The Freewheelin' Bob Dylan",
#   1975: "Blood on the Tracks",
#   1997: "Time Out of Mind"
# }

# Use .keys() to loop through and print out all the release years
# for year in dylan_albums.keys():
# print(year)

# Use .values() to loop through and print out all the album names

# Use .items() to loop through and print out both the release year and album name

# Use the 'in' keyword to check if a particular year or album is in the dictionary (pick any year and any album)
# Remember the keyword by default checks only the keys, not the values.
# If you want to check if a particular value (in this case, an album name),
# you need to specify that you're searching within the dictionary's values.

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 4. Remove duplicates
# Remove duplicates from the following dictionary:
# person = {
#   'first': 'Jeff',
#   'name': 'Jeff',
#   'last': 'Smith',
#   'last_name': 'Smith',
#   'state': 'CA',
#   'age': 55
# }

# Steps:
# - Create a dict person
# - Create an empty dictionary result = {}
# - Make a for loop to iterate over person dictionary
# - If item’s value not in result dict, add key value part into result.

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 5. Find the highest score
# Create a Python function named find_max_score that takes a dictionary of names and scores as an argument.
# The function should return the name and score of the person with the highest score in the form of a dictionary.

# Sample test_scores dictionary
# test_scores = {
#   'James': 83,
#   'Julia': 91,
#   'Ryan': 90,
#   'Maria': 80,
#   'David': 79,
#   'Adam': 96,
#   'Jennifer': 97,
#   'Susan': 77
# }

#  Find the person with the highest test score and display both their name and score

# Steps:
# - Define a function called find_max_score that takes one argument, scores_dict, which is a dictionary of names
#   (as keys) and scores (as values).
# - Create an empty result variable
# - Assume the initial maximum score is 0
# - Iterate over each key-value pair in the test_scores, using the .items() method
# - Check if the current score (v) is >= to the current maximum score
# - If so, update the max score and assign the key-value pair to the result
# - Return result and test the function
