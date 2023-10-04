# You’re given an array. Find if given array is in a form of mountain or not.

# There exists some index i such that:
# arr[0] < arr[1] < ... < arr[i]
# arr[i] > arr[i + 1] > ... > arr[-1]

# Basically, find if there is an increasing subarray followed by a decreasing subarray
# [3, 5, 5] -> false
# [3, 4, 5, 2] -> true

# The length of the list is longer or equal to 3.

def is_mountain_array(arr):
    # Check the increasing sub-array
    i = 1
    while i < len(arr) and arr[i - 1] < arr[i]:
        i += 1

    if i == 1 or i == len(arr):
        return False

# Check the decreasing sub-array
# Your code here
