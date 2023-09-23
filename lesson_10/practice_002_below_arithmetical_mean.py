# When given a list, the program should return a list of all the elements
# below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.

# Example: [1, 3, 5, 6, 4, 10, 2, 3]
# Arithmetical mean: 4.25
# Output: [1, 3, 4, 2, 3]

# Steps
# To find the arithmetical mean, use the sum () and the len () functions.
# Iterate through each element in the array.
# Create an empty list to store elements below the arithmetic mean.
# Check if the element is below the arithmetic mean.
# If yes, append it to the final_list.
# Return the final list of elements below the arithmetic mean.

# Pre-code
def below_arithmetical_mean(arr):
    arithmetical_mean = sum(arr) / len(arr)
