# Conditionals Reference

## `if` statement

```python
# Checks if the user is old enough to vote
age = 19
if age >= 18:
    print("You are eligible to vote.")
```

## `else` statement

```python
# Checks if a number is positive or negative
num = -5
if num >= 0:
    print("The number is positive.")
else:
    print("The number is negative.")
```

## `elif` statement

```python
# Checks the time of day and gives a greeting
time = 16  # 24-hour format
if time < 12:
    print("Good morning!")
elif time < 18:
    print("Good afternoon!")
else:
    print("Good evening!")
```

## Nested Conditionals

```python
# Checks if a student passed a course
grade = 80
attendance = 90  # percentage

if grade >= 60:
    if attendance >= 75:
        print("You passed the course!")
    else:
        print("You passed based on grade, but failed due to low attendance.")
```

## Conditional Operators

```python
# Initialize variables for demonstration
a = 10
b = 20
```

### Equality (==)

```python
if a == 10:
    print("a is equal to 10")
```

### Not Equal (!=)

```python
if a != b:
    print("a is not equal to b")
```

### Less Than (<)

```python
if a < b:
    print("a is less than b")
```

### Greater Than (>)

```python
if b > a:
    print("b is greater than a")
```

### Less Than or Equal To (<=)

```python
if a <= 10:
    print("a is less than or equal to 10")
```

### Greater Than or Equal To (>=)

```python
if b >= 20:
    print("b is greater than or equal to 20")
```

## Boolean Operators

### `and` operator

Both conditions must be `True`

```python
# Checks if a candidate is qualified for a job
experience = 5  # years
education = "Bachelor's"  # degree type
if experience >= 3 and education == "Bachelor's":
    print("You are qualified for this job.")
```

### `or` operator

At least one of the conditions must be `True`

```python
# Checks if a store is open based on day and time
day = "Saturday"
time = 9  # 24-hour format

if day == "Sunday" or time < 10:
    print("The store is closed.")
else:
    print("The store is open.")
```

### `not` operator

Invert the value of the condition

```python
is_raining = False

if not is_raining:
    print("It's a sunny day!")
```

## Sample Exercises

### Even or Odd Problem

The "Even-Odd" problem involves determining whether a given number is even or odd by checking its divisibility by 2.

```python
# Initialize the variable 'number' with the value 42
number = 42

if number % 2 == 0:  # Check if 'number' is divisible by 2
    # If the condition is True, print "Even"
    print('Even')
else:  # If the condition is False, print "Odd"
    print('Odd')
```

One-line solution

```python
number = 42

print('Even' if number % 2 == 0 else 'Odd')
```

### FizzBuzz Challenge

FizzBuzz is a programming challenge that involves printing the word "Fizz" for numbers divisible by 3, "Buzz" for numbers divisible by 5, and "FizzBuzz" for numbers divisible by both 3 and 5, all within a certain range.

```python
# Initialize 'number' to 9
number = 9

if number % 15 == 0:  # Check if number is divisible by both 3 and 5
    print('FizzBuzz')
elif number % 3 == 0:  # Check if number is divisible by 3 only
    print('Fizz')
elif number % 5 == 0:  # Check if number is divisible by 5 only
    print('Buzz')
```

Using `and` operator

```python
# Initialize 'number' to 9
number = 9

if number % 3 == 0 and number % 5 == 0:  # Check if number is divisible by both 3 and 5
    print('FizzBuzz')
elif number % 3 == 0:  # Check if number is divisible by 3 only
    print('Fizz')
elif number % 5 == 0:  # Check if number is divisible by 5 only
    print('Buzz')
```