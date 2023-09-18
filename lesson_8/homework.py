# Homework Lesson 8 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# Challenge 1
# Two Lowest Elements
#
# Your task is to write a program that takes a list of numbers and finds
# the two smallest numbers in it. The two smallest numbers can be equal to
# each other or different.
#
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
#
# Hint: Start with sorting the list

arr = [5, 2, 9, 1, 5, 6]
# Your code here

# ---------------------------------------------------------------------

# Challenge 2
# Remove Spaces
#
# Imagine, you're trying to organize your files, and you notice that one
# of your file names contains several spaces, which could lead to errors
# or difficulties in file management. Your task is to remove all the spaces
# from the given file name using a `for` loop.
#
# Hint: Loop through each character and check if a character is NOT a space.
# If it’s not, add the character to the new file name. This way, you will
# exclude all spaces.

file_name = "My Summer Photos 2023"
# Your code here

# ---------------------------------------------------------------------

# Challenge 3
# Sum of digits
#
# Compute the sum of digits in all numbers from 1 to 5.
# When the result gets a number n, find the sum of digits
# in all numbers from 1 to 5.
#
# Example: number = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

# Initialize 'number' variable to 5. This is the number up to which we will calculate the sum.
n = 5

# Initialize 'result' variable to 0. This variable will hold the sum.

# Iterate through the range starting from 1 up to 'number + 1'.

# Add the current value of 'i' to 'result'

# Print the sum of integers from 1 to 'number'


# ---------------------------------------------------------------------

# Challenge 4
# Isogram
#
# Write a Python program that checks if a given word is an isogram
# — an isogram is a word with no repeating letters, such as ‘cat’, ‘taco’, or ‘dog’.
#
# Example:
# For "cat", print True
# For "mom", print False
#
# Choose any word, you’d like to check.
# If it’s an isogram, print True. If it’s not an isogram, print False.
#
# Hints:
# Use a for loop to iterate over every letter and conditional statements to check the condition
# Use the count() method (think how it can help you solve this problem!)


# ---------------------------------------------------------------------

# Challenge 5
# Repeat digits
#
# Given a string “312”, your task is to create a new string where each
# digit from the original string is repeated a number of times equal to its value.
#
#
# For the input string "312," your program should output "333122."
#
# Hints:
# To make a digit appear as many times as its value (like turning “3” into "333"),
# you have to multiply the string by a number.
# In Python, multiplying a string by a number repeats the string that many times.
# Since our digit is a string, we need to convert it to a number using int() so we can repeat it correctly.
# Once the digit is a number, just multiply the character by this value to get the repeated string.

string = "312"

# Initialize an empty string called 'result' to store the result

# Loop through each character in the string

# Inside the loop, turn the character into a number using int()
# and store it as a current_num variable

# Multiply the character by its number value
# and add the repeated character to 'result'

# Print the final result
