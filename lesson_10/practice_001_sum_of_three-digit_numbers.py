# A program gets a three-digit number and has to sum up all its digits.

# For example, if a number is 349,
# the code has to print the number 16,
# because 3 + 4 + 9 = 16.

# Steps
# - Define a function named sum_of_three that takes a single argument called number.
# - Initialize a variable called result to store the sum of the last three digits.
# - Use a for loop and range to iterate three times.
# - Use the modulus operator % to get the last digit. Then add the last digit of the number to result.
# - Remove the last digit from the number using floor division.
# - Return the sum of the last three digits.

# Pre-code:
def sum_of_three(number):
