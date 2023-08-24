# Numbers Reference

## Arithmetic Operations

### Addition

```python
sum_result = 5 + 3
print("5 + 3 =", sum_result)  # Output: 5 + 3 = 8
```

### Subtraction

```python
difference_result = 10 - 4
print("10 - 4 =", difference_result)  # Output: 10 - 4 = 6
```

### Multiplication

```python
product_result = 3 * 7
print("3 * 7 =", product_result)  # Output: 3 * 7 = 21
```

### Division

```python
division_result = 15 / 3
print("15 / 3 =", division_result)  # Output: 15 / 3 = 5.0
```

### Modulus (remainder of a division)

```python
remainder = 17 % 5
print("17 % 5 =", remainder)  # Output: 17 % 5 = 2
```

### Exponentiation

```python
power_result = 2 ** 3
print("2 ** 3 =", power_result)  # Output: 2 ** 3 = 8
```

### Floor Division (performs division and rounds down to the nearest integer)

```python
floor_result = 17 // 5
print("2 ** 3 =", power_result)  # Output: 2 ** 3 = 8
```

## Operator Precedence

- Parentheses have the highest precedence.
- Exponentiation has the next highest.
- Multiplication, division, and floor division have the same precedence.
- Addition and subtraction have the lowest precedence.

```python
x = 5
y = 3
z = 2

result = x + y * z  # Multiplication has higher precedence than addition
print("x + y * z =", result)  # Output: x + y * z = 11

result = (x + y) * z  # Parentheses enforce addition before multiplication
print("(x + y) * z =", result)  # Output: (x + y) * z = 16

result = x ** y / z  # Exponentiation has higher precedence than division
print("x ** y / z =", result)  # Output: x ** y / z = 41.666666666666664

result = x ** (y / z)  # Parentheses enforce exponentiation before division
print("x ** (y / z) =", result)  # Output: x ** (y / z) = 11.180339887498949
```

## Assigning and Reassigning Variables

```python
# Assigning a value to a variable
x = 5

# Reassigning a variable with a new value
x = 10
```

## Naming Variables

- Variable names must start with a letter or an underscore
- They can contain letters (a-z and A-Z), numbers, and underscores
- Variable names are case-sensitive (`variable` is different than `Variable`)
- Some names are used as [reserved words](https://docs.python.org/3/reference/lexical_analysis.html#keywords) and can not be used as variable names

```python
speed = 50
my_variable = "Hello"
_test_failes = 23
name_1 = "John"
```

## Handling Error Messages

- When something doesn't work as expected during the execution of the code, Python will raise an **exception**
- Reading the error message will provide you hints about how to solve the problem

```python
>>> 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

```python
>>> * 5
  File "<stdin>", line 1
SyntaxError: cant use starred expression here
```

## Basic Data Types


### Strings

```python
text = "Hello, world!"
```

### Integers

```python
int_value = 42
```

### Floats

```python
float_value = 15.21
```

### Booleans

```python
enabled = True
```

## Checking data type of value

Use `type()` function:

```python
text = "Hello, world!"
int_value = 42
float_value = 15.21
enabled = True

print(type(text))  # Output: <class 'str'>
print(type(int_value))  # Output: <class 'int'>
print(type(float_value))  # Output: <class 'float'>
print(type(enabled))  # Output: <class 'bool'>
```

## Casting and Converting Data Types

Convert to integer, use `int()` function:

```python
float_number = 3.14
int_number = int(float_number)
print(int_number)  # Output: 3
```

Convert to float, use `float()` function:

```python
int_number = 5
float_number = float(int_number)
print(int_number)  # Output: 5.0
```
