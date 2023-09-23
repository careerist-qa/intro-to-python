# Consider a list (array) of non-negative integers.
# A second list is formed by shuffling the elements of the first list and deleting a random element.
# Given these two lists, find which element is missing in the second array.

# Example
# List 1: [1, 2, 3, 4, 5, 6, 7]
# List 2: [3, 7, 2, 1, 4, 6]
# Output: 5 is the missing number

# Steps

# Create a function find_missing_number with two list inputs, arr1 and arr2.
# Sort both lists to make comparison easy.
# Loop through the length of arr2 (the shortest list).
# Create a condition to check if the element in arr1 is not equal in arr2.
# If the elements are different, you found the mismatched number in arr1! Return it.
# If the loop completes without finding any unequal elements,
# it means the missing element is the last number. Return it.

# Pre-code
def find_missing_number(arr1, arr2):
