# Strings Reference

## Creating strings with single quotes

```python
single_quotes = 'This is a string.'
```

## Creating strings with double quotes

```python
double_quotes = "This is also a string."
```


## Creating strings with triple quotes for multi-line strings

```python
multi_line = '''This is a
string
in multiple
lines'''
```

```python
multi_line = """This is also a
string
in multiple
lines"""
```

## Escape characters

Use escape characters to to include special characters in a string such as an apostrophe or quotation marks. Put the escape character before this special symbol.

### Using escape for apostrophe

```python
escaped_apostrophe = 'He said, "It\'s sunny today!"'
```

### Using escape for quotation marks

```python
escaped_quotes = "She said, \"Hello!\""
```

## Code comments

```python
# Comments are used to add notes and explanations to code. They are not executed
# They help other developers (and yourself) understand the purpose of the code

# This variable stores the user's name.
user_name = "Alice"

# This variable stores the user's age.
user_age = 25

# This line prints a greeting message using the user's name and age.
print("Hello,", user_name, "! You are", user_age, "years old.")

#print("Hello")
# the previous line will not be executed, as it is a comment
```

## Converting to strings

```python
number = 42  # Integer value
print(number)  # Output: 42

number_str = str(number)  # Convert int to a str
print(number_str)  # Output: "42"
```

```python
number = 42.32  # Float value
print(number)  # Output: 42.32

number_str = str(number)  # Convert float to a str
print(number_str)  # Output: "42.32"
```

## Receiving user input

`input()` function is used to receive user input from the console.

```python
name = input("Enter your name: ")  # type something and press Enter
```

In this case, we prompt the user to enter their name and store it in the 'name' variable.

```python
age = input("Enter your age: ")  # Type 25 and press Enter
print(type(age))  # Output: <class 'str'>
```

`input()` receives only strings. You are responsible to convert the input to the type you want

```python
str_age = input("Enter your age: ")  # Type 25 and press Enter
age = int(str_age)
print(type(age))  # Output: <class 'int'>
```

**If you try to convert an invalid value, a `ValueError` will be raised**

## Formatting Strings

### Concatenation

```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print(full_name)  # Output: "John Doe"
```

### .format()

The `.format()` method is used to format strings by replacing placeholders with values.

```python
fruit = "apple"
quantity = 3
formatted = "I have {} {}s.".format(quantity, fruit)

print(formatted)  # Output: "I have 3 apples"
```

```python
first_name = "Thomas"
last_name = "Edison"
formatted = "{0} {1}".format(first_name, last_name)

print(formatted)  # Output: "Thomas Edison"

formatted = "{1} {0}".format(first_name, last_name)

print(formatted)  # Output: "Edison Thomas"
```

```python
fruit = "apple"
quantity = 3
formatted = "I have {quantity} {fruit}s.".format(quantity=quantity, fruit=fruit)

print(formatted)  # Output: "I have 3 apples"
```

### f-strings

F-strings allow us to insert variables directly into strings.

```python
name = "Alice"
age = 30
formatted = f"My name is {name} and I am {age} years old."

print(formatted)  # Output: "My name is Alice and I am 30 years old."
```

## String Methods and functions


- `str.upper()` - Return a copy of the string with all the cased characters 4 converted to uppercase.

```python
text_upper = text.upper()    # Output: "PYTHON IS FUN!"
```

- `str.lower()` - Return a copy of the string with all the cased characters 4 converted to lowercase.

```python
text_lower = text.lower()    # Output: "python is fun!'
```

- `str.title()`` - Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.

```python
text_title = text.title()    # Output: "Python Is Fun!'
```

- `.replace(old, new)` - Return a copy of the string with all occurrences of substring `old` replaced by `new`.

```python
text = "Programming Java is fun!"
replaced_text = text.replace("Java", "Python")

print(replaced_text)  # Output: "Programming Python is fun!"
```

- `len(string)` - return the length of a string
```python
text = "Hello World!"
length = len(text)

print(length)  # Output: 12
```

- `str.count(substring)` - Return the number of non-overlapping occurrences of `substring` in the string.

```python
text = "is that an island?"
count_is = text.count("is")

print(count_is)  # Output: 2
```

## Indexing and slicing

Indexing and slicing allow us to access specific characters or portions of strings (substrings).

```python
text = "Python is fun!"
char_at_index_7 = text[7]   # Output: "i'
substring = text[0:6]       # Output: "Python'
every_second = text[::2]    # Output: "Pto sfn' (every second character)

# Using negative indexing to access characters from the end of the string
last_char = text[-1]       # Output: "!'
substring_end = text[-4:]  # Output: "fun!'

# Reversing a string using slicing with a step of -1
reversed_text = text[::-1]  # Output: "!nuf si nohtyP'

# Slicing the reversed string
reversed_text = text[13:9:-1]  # Output: "only !nuf"
```