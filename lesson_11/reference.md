# Dictionaries Reference

## Creating an empty dictionary

```python
# Create the empty dictionary
my_dictionary = {}

# Add items afterwards
my_dictionary['name'] = 'Janette'
my_dictionary['age'] = 55
my_dictionary['email'] = 'janette@company.com'
```

## Creating a pre-populated dictionary

```python
my_dictionary = {
    'name' : 'Janette',
    'age' : 55,
    'email' : 'janette@company.com'
}
```

## Accessing values

Use the name of the dictionary and the key in square brackets `[]`
like you would do with lists. You can also do it with nested
dictionaries.

```python
person = {
  'name': 'Joseph',
  'location': {
      'city': 'Houston',
      'state': 'TX'
  }
}

# Prints: 'name': 'Joseph','location': {'city': 'Houston','state': 'TX'}
print(person)                      

# Prints: {'city': 'Houston', 'state': 'TX'}
print(person["location"])          

# Prints: Houston
print(person["location"]["city"])
```

## Update values in the dictionary

```python
test_scores = {
    'james': 83, 
    'julia': 91, 
    'ryan': 90, 
    'maria': 80
}

# Change Julia's score to 100
test_scores['julia'] = 100

# Use .update() to add and/or update multiple values.
revised_scores = {
   'julia': 95,    # Will be updated to 95
   'ryan': 80,     # Will be updated to 80
   'joseph' : 85   # Will be added
}

test_scores.update(revised_scores)
```

## Remove a value from the dictionary

```python
test_scores = {
   'james': 83,
   'julia': 91,
   'ryan': 90,
   'maria': 80
}

# This will eliminate the key:value from the dictionary for the key 'julia'
del test_scores['julia']
```

## Iterating over dictionaries

View objects `keys()`, `values()` and `items()` are useful to iterate 
over those element components.

- `keys()` returns an iterable with the keys in the dictionary.
- `values()` returns an iterable with the values in the dictionary.
- `items()` returns an iterable of touples with both the key and value for each
element in the dictionary.

```python
# Year: Title
films = {
  2018: "Black Panther",
  2019: "Avengers: Endgame",
  2020: "Bad Boys for Life"
}

# Using .keys() gives us the keys.
for year in films.keys():
   print(year)

# Using .values() gives us the titles.
for title in films.values():
   print(title)

# Using .items() gives us both as a tuple (first the key, then the value)
for year, title in films.items():
   print(f"{year} was released in {title}.")
```

## Check if something is in the dictionary

Use `in` or `not in` as you would with lists.

```python
# Year: Title
films = {
  2018: "Black Panther",
  2019: "Avengers: Endgame",
  2020: "Bad Boys for Life"
}

# Using `in` directly on the dictionary will check the keys, 
# just as with keys(). These two are equivalent.
print(2018 in films)                # Prints: True
print(2018 in films.keys())         # Prints: True

# Check in the values
print('Avatar' in films.values())   # Prints: False
```

