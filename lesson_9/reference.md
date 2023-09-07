# Functions Reference

## Defining a Basic Function

- The most basic function doesn't return anything.
- Any function must be declared before its call. If the `def` of the function is after its
call, you will get a `NameError` since you're asking Python to call a function it has not seen yet.

```python
def function_name():
    # Function body, or "pass" as a placeholder
    pass
```

## Returning a value

You can have the function return a value (the result of a calculation, or True / False, or
anything you want) using the `return` keyword. Using `return` not only returns the value but also
stops the execution of the function.

```python
def sum_values(a, b):
    c = a + b
    return c

my_sum = sum_values(1, 2)
print(my_sum) # Prints: 3
```

A common usage pattern is to return `True / False` to help you validate something.

```python
# Define a function that returns True if the provided name starts with 'a' or 'A'
def starts_with_a(name):
    first_letter = name[0:1]

    if first_letter in ['a', 'A']:
        return True
    else:
        return False

# Pretend we have a list with names we need to validate
names = ['Joseph', 'Tom', 'Albert', 'Kelly']

# For each name in the list, call the validator and if the 
# result (return value) is True, print the message.
for name in names:
    if starts_with_a(name):
        print(f"{name} starts with a")
        
# This will print: Albert starts with a
```

## Parameter Definition

Use variables inside the parentheses of the function definition to receive values from the
function call.

```python
# Single parameter
def function_name(parameter1):
    pass

# Multiple parameters, comma separated
def function_name(parameter1, parameter2):
    pass

# You can define default values for parameters. Parameters with a 
# default value become optional.
def function_name(parameter1, parameter2="Default value"):
    pass
```

## Calling Functions

_Call_ (execute) a function by using its name with parentheses.

```python
# Call a function that doesn't have any parameters or all its parameters are optional
function_name()

# Call a function with parameters in the order as defined
function_name(1, 2)

# You can call them out of order by using the parameter names
function_name(parameter2=2, parameter1=1)
```

## Parameters or Arguments? 🤔

When talking about functions most people use _parameters_ and _arguments_ interchangeably, 
and that's okay, but you should understand the subtle difference.

- We call the _variables_ in the function _definition_ **parameters**.
- We call the _values_ in the function _call_ **arguments**.

```python
# Here, "name" is a PARAMETER.
def greeting(name):
    print(f"Hello, {name}!")

# Here, "Joseph" is an ARGUMENT.
greeting("Joseph")
```

## Using other structures inside Functions

You can use almost any valid python code inside functions like `if` statements, `for` / `while`
loops.

```python
# Declare a greetings function that expects a list of names as parameter.
def greetings(name_list):
    for name in name_list:
        print(f"Hello, {name}!")

# Create a list with a couple names
names = ["Joseph", "Tom"]

# Call the greetings function and pass the names list as an argument
greetings(names)

# Prints:
# Hello, Joseph!
# Hello, Tom!
```

## Calling Functions from other Functions

You can call functions from inside other functions if you need to.

This example only greets people with names starting with `T`. See if you can follow the flow.

```python
def greeting(name):
    print(f"Hello, {name}!")
    
def name_starts_with_t(name):
    if name[0:1] in 'Tt':
        return True
    else:
        return False

def process_names(name_list):
    for name in name_list:
        if name_starts_with_t(name):
            greeting(name)
        
names = ["Joseph", "Tom", "Kelly"]
process_names(names)

# This will only greet Tom
```