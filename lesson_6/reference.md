# Lists Reference

## Creating a List 

```python
# Creates an empty list
my_list = []

# Creates a pre-populated list
my_list = ["Something", 1, 2.00, True, [100, 200]]
```

## Adding Elements ➕

```python
# At the very end, using append()
my_list.append("Something")

# ADVANCED: At a specific position, using insert()
my_list.insert(0, "Something") # Index 0, so this inserts the element at the beginning.
my_list.insert(3, "Something") # Index 3, so this inserts the element just after index 2.
```

## Removing Elements ✄

This section mentions the `pop()` method, which also removes an element from the `list` like `del` does. The main difference with 
`del` is that `pop` returns the value that is being removed, in case you want to do something else with it. 

```python
# From anywhere, without returning a value
del my_list[0] # Removes the first element (index 0).
del my_list[2] # Removes index 2 (meaning the THIRD element).

# From anywhere, returning a value
some_element = my_list.pop()  # Removes the last element, and returns its value.
some_element = my_list.pop(2) # Removes element at index 2, and returns its value.

# Negative indexes are okay to use also, to delete or pop elements from the end.
del my_list[-1]  # Removes the last element.
del my_list[-2]  # Removes the previous to last element.

some_element = my_list.pop(-1)  # Pops (delete and return its value) the very last element.
some_element = my_list.pop(-2)  # Pops (delete and return its value) the second to last element.

# Remove by value. Will remove the first element it finds.
my_list.remove("some_value")
```

## Check if an Element exists (Boolean Check) 🔍

```python
my_list = [100, 200, 300]

# This prints YES, as 100 is part of the list.
if 100 in my_list:
    print("YES")
else:
    print("NO")

# This prints NO, as 400 is NOT part of the list.
if 400 in my_list:
    print("YES")
else:
    print("NO")
```

## Sorting 🔀

```python
# Sort a list, modifying the original list.
my_list.sort()
my_list.sort(reverse=True) # Descending (reversed) order.

# Sort a list, returning a new copy and leaving the original unchanged.
sorted_list = sorted(my_list)
sorted_list = sorted(my_list, reverse=True) # Descending (reversed) order.
```

## Slicing 🔪

```python
# Without arguments, the slicer doesn't slice anything.
my_slice = my_list[:]   # Doesn't slice, just return a copy.
my_slice = my_list[::]  # Same

# Get the first two elements.
my_slice = my_list[0:2]  # Returns elements on indexes 0 and 1

# Get the second, third and fourth elements.
my_slice = my_list[1:4]  # Returns elements on indexes 1, 2 and 3

# Stepped slicing. Get every N items.
my_slice = my_list[::2] # The whole list, every 2 indexes: 0, 2, 4, 6
my_slice = my_list[0:4:2]  # Get a slice of indexes 0, 1, 2, and 3, and THEN do the steps to return 0 and 2

# Use negative steps to return the list stepped in reverse (can be a little confusing).
my_slice = my_list[::-1]  # This just returns a reversed list.
my_slice = my_list[::-2]  # This returns a reversed list, every 2 elements, starting from the end.
```

## Reversing 🔁

This is not the same as reverse sorting (like in the previous section). Reverse sorting actually **sorts** the list 
before reversing it. Using `reverse()` or `reversed()` **do not sort** the list - only **reverse** it. 

🔥🔥🔥
Note that to use `reversed()` it needs to be wrapped with `list()`. This is called *casting* and it's an advanced
topic, but just know that you need to do it this way in order to use `reversed()` as shown.
🔥🔥🔥

```python
# Reverse (flip) the list, modifying the original.
my_list.reverse()

# Reverse the list. Return a new reversed copy and leave the original unchanged.
reversed_list = list(reversed(my_list))

# Reverse the list using the slicer with a step of -1, as mentioned in the previous section.
reversed_list = my_list[::-1]
```

## Aggregators ⚙

```python
# The lowest value in a list. NOT the lowest index. Only works with elements of the same type (numbers and strings).
min([3,2,5]) # 2
min(['C', 'B', 'D', 'A'])  # A

# The highest value. Same rules apply.
max([3,2,5]) # 5
max(['C', 'B', 'D', 'A'])  # D

# The SUM of all the values. Very helpful if you have a list of numbers and need to add them up quick!
sum([1, 2, 3]) #6
sum([1, 2, 3, True]) # 7, since True is like 1.
```

## Helpers 💪🏻

```python
# If you need to know how many elements a list has.
len([1, 2, 3, 4, 5]) # The list contains 5 numbers.
len([1, 2, 3], [4, 5, 6])  # The list contains 2 lists.

# If you want to know what is the index of a given element. It will return the first one it finds.
my_list = ["Eric", "Joseph", "Tom", "Joseph"]
my_list.index("Joseph") # Returns 1.

# If you want to count how many times a value is present in a list.
my_list = [100, 200, 200, 300, 300, 300]
my_list.count(200) # Returns 2.
```