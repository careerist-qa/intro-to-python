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
