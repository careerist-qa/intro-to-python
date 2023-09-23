# Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z and it's not a palindrome.

# Example:
# "rakdar" is almost a palindrome.
# "radario" is not almost a palindrome.

# Steps
# Create a for loop to iterate over each index in the string (range).
# You can find the length of the string with the built-in function len()
# Slice current string from the first character until i and concatenate it with i+1 until the end of the string.
# If the string is equal to the reversed string, return True
# If it’s not almost a palindrome, return False

# Pre-code
def is_almost_palindrome(s):
