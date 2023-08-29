# Loops Reference 🤯

## Types of Loops

### `for` Loops

Best suited for cases when you have a finite set of elements you want to iterate over, like a 
`string`, `list`, `dictionary` or other collections.

**Example use case**: Send a notification to each of these 1,000 emails. 

### `while` Loops

Best suited for cases when you need to keep doing something for as long as a condition remains 
true.

**Example use case**: Keep asking the user for input until they type `end`

## Loopable Objects

I call them loopable, but the right word is **_iterable_**. These are **some** types of objects most
commonly looped over using `for` loops:

- Strings
- Ranges
- Lists
- Tuples
- Sets
- Dictionaries

## Basic `for` Loop Structure

`item`  Can be any name. This is the current element being _in scope_.
`iterable` The object containing the elements we're iterating over.
`body` The action or actions we want to do for the `item` in scope.

```python
for <item> in <iterable>:
    <body>
```

## Basic `while` Loop Structure

`condition` Every loop, this gets evaluated. If `True` then the loop executes the `body`. If condition is
`False`, the loop exits.
```python
while <condition>:
    <body>
```

## Ranges

The `range()` function allows you to generate sequential numbers.

Syntax:
```python
# Single argument
range(stop)

# Multiple argument
range(start, stop, optional_step)
```

Arguments:

- `start` The first element of the sequence, **inclusive**.
- `stop` The last element of the sequence, **exclusive**.
- `step` (optional) Every **N** numbers will be returned. See examples.

Examples:
```python
range(5)        # Generates 0, 1, 2, 3, 4
range(0, 5)     # Also generates 0, 1, 2, 3, 4
range(1, 10)    # Generates 1, 2, 3 ... 9
range(2, 7, 2)  # Generates even numbers 2, 4, 6
range(1, 7, 2)  # Generates odd numbers 1, 3, 5
```

## Break 🛑

The `break` keyword makes the loop stop and exit **immediately**. Anything after `break` in the loop
`body` will not be executed.

It can be used in `for` and `while` loops.

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print("This will only print the first number")
    break
```

An example using a `while` loop.

```python
while True:
    print('This will only print once')
    break
```

## Counter Pattern

Sometimes we need to keep track of how many times a loop has been executed. 
We can use a counter variable for this. The counter variable can have any name.

```python
# Declare a numeric variable that we can use to track iterations
counter = 0

# Set up a loop that increments a counter every iteration
for character in "word":
   counter = counter + 1

# This will print out the number of characters in "word"
print(counter)
```
