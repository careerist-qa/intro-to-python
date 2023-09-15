# Homework: Functions

🔥 **Read carefully until the end before you start solving the exercises.** 🔥

## Practice the Basics 💪🏻

### Basic Function

Define a basic function that only prints `Hello`. Create the definition using `def` and the
call that executes it.

### Basic Function with Parameters

Define a basic function that prints a greeting taking a given name.

### Basic Function with Default Values

Define a basic function that prints a greeting for a name, but if none is given, use `stranger` 
instead of the name, so it behaves like this:

```python
greeting() # Prints: Hello, stranger!
greeting('Tom') # Prints: Hello, Tom!
```

### Multiple Parameters

Define a function that takes two parameters, add them up and prints the `sum`.

```python
add(1, 2) # Prints: The sum of 1 + 2 = 3
add(1) # Prints (default values might be useful): The sum of 1 + 0 = 1
```

### Parameters out of order

Define a function that takes a `first_name` and a `last_name` and prints a `full_name`. Define
the function and create the function call in such a way that `first_name` and `last_name` can be
given in any order and the printed `full_name` would still be correct.

```python
full_name("Nelson", "Mandela") # Prints: Nelson Mandela
full_name(first_name="Nelson", last_name="Mandela") # Prints: Nelson Mandela
full_name(last_name="Mandela", first_name="Nelson") # Prints: Nelson Mandela
```

### Returning Values

Define a validator function that you can use to determine if a word is longer than 8 characters.

**Tip**: Validator functions return `True / False` which we can use to do thins like print a message.

## Exercises 🏋🏻‍♀️

### FizzBuzz 🐝

You've already solved the FizzBuzz problem, where you print "Fizz" for multiples of 3, "Buzz" for multiples of 5, 
and "FizzBuzz" for multiples of both 3 and 5. 

Now, your task is to take your existing FizzBuzz code and wrap it into a function called fizzbuzz.

#### Requirements
- Create a function named fizzbuzz that takes a single argument, number.
- If the number is a multiple of both 3 and 5, the function should return: `FizzBuzz`
- If the number is a multiple of 3, the function should return: `Fizz`
- If the number is a multiple of 5, the function should return: `Buzz`
- Otherwise, the function should return the number.

```python
# Pre-code
number = 15

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)
    
# Wrap it into a function
def fizzbuzz (???):
    # Your code here
    pass

# Call the function
```

### Anagram

Your next challenge is to implement a function that checks if two given strings are anagrams of each other. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase. 
For example, "listen" is an anagram of "silent".

#### What You Need to Check
- The two strings must have the same length.
- The sorted form of the first string must be equal to the sorted form of the second string.

```python
# Pre-code
# Create a function named anagram. The function should take two strings as arguments
 def ???

    # Check if the lengths of the strings are equal. If not, return False.
    if ???
        ???

    # Sort both strings and compare. If they are equal, return True.
    elif ???
        ???
    else:
        ???

# Test your function with this string
test_str1 = 'abcde'
test_str2 = 'edcba'

# Call your function here to test
```

### Find Max number

Create a function to find the largest number in a list _**without** using the build-in `max()` function_.

- Define a function called `find_max` that takes a list of numbers as an argument.
- Initialize a variable `result` and set it to the 1st item of the list using `[0]`
  - This variable will hold the largest number as we iterate through the list.
- Loop through each number in the list.
- Check `if number > result`
  - If it is, update `result` with the new greater number.
- `return result`

```python
# Define your function here

# Test the function with a sample list of numbers.

# Output should be the maximum number in the list.
```

### Even/Odd Checker Function

Your task is to write a function that determines if a given integer is even or odd. 
The function should print `Even` for even numbers and `Odd` for odd numbers.

#### What You Need to Check

- Determine whether the input number is even or odd.
- An even number can be exactly divided by 2 without a remainder.
- An odd number leaves a remainder of 1 when divided by 2.

```python
# Define a function is_even_odd(number) here

# Test the function calling it using a variety of numbers
# 1... 10... 5,5... 9...
```
