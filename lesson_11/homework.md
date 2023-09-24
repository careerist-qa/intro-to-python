# Homework: Dictionaries 📚

## Practice the Basics

🔥 **Read carefully until the end before you start solving the exercises.** 🔥

## Practice the Basics 💪🏻

### Basic Dictionary

Create an empty dictionary for your friends and then add elements. 
Make the key their email and the value their name.

When you're done, create the same dictionary as a pre-populated dictionary.

### Nested Dictionary

Create a nested dictionary for a list of 5 company employees.

The key should be their employee id (an integer from 1-5 will do) 
and the value should be a dictionary with the name, 
department and salary of the employee.

### Accessing Values

Use the previous nested dictionary and write some print statements that
will answer the following:

- Print a list of the employee IDs
- Print the employee details for employee with the ID 3.
- Loop over the employees and print all their names and salaries.

### Updating Values

We have the following dictionary with employee salaries.

```python
salaries = {
    'james' : 10000,
    'tom' : 15000,
    'ryan' : 16000,
    'julia' : 17000
}
```

We need to increase everyone's salary by `1,000` and also add a new
employee `joseph` with a salary of `18,000`. 

Please come up with a way to do this using `update()` 

### Deleting Values

You remember those employees from `Updating Values` section? Well,
Julia got fired, so we need to remove her name from the `salaries` 
dictionary. How would you do that?

### Iterating over Dictionaries

Given the list of movies below, please use view objects (`keys(), 
values(), items()` - where necessary) to answer the questions:

- Is Black Panther in the list of movies?
- Is there any movie for the year 2021?
- Print a message for each element that shows the year, the title and
the position in the dictionary (1-5). Hint: use a counter.

```python
films = {
   2016: "Star Wars: Episode VII - The Force Awakens",
   2017: "Star Wars: Episode VIII - The Last Jedi",
   2018: "Black Panther",
   2019: "Avengers: Endgame",
   2020: "Bad Boys for Life"
}
```