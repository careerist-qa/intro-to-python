# Write a program that takes three user's inputs:
# - A sentence
# - A word to replace
# - Letter to count

# You need to provide two outputs:
# - The sentence replacing all "word to replace" with REPLACED
# - The number of occurrences of the given letter to count in the sentence

sentence = input("Enter a sentence: ")
new_word = input("Enter the word to replace: ")
letter = input("Enter the letter to count: ")

# Example
# Enter a sentence: I love cats and dogs, but cats are my favorite.
# Enter the word to replace: cats
# Enter the letter to count: o

# Expected output:
# I love REPLACED and dogs, but REPLACED are my favorite.
# 3
