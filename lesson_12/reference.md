# Classes Reference

## Basic Class Syntax

```python
class SomeClassName:
    pass
```

## Create an Instance

```python
class Animal:
    pass

dog = Animal()
cat = Animal()
```

## Add Instance Attributes

```python
class Animal:
    pass

dog = Animal()
dog.lets = 4
dog.name = 'Fido'
```

## Instance Methods

All methods use `self` as the first argument. 

```python
class Dog:
    def bark(self):
        print(f"Woof!")

fido = Dog()
fido.bark() # Prints: Woof!
```

## Constructor

A method called `__init__` that will get executed when an instance is created.

```python
class Car:
    def __init__(self):
        print('A Car instance has been created!')
        
mustang = Car() # Prints: A Car instance has been created!        
```

## Constructor with Parameters

```python
class Car:
    def __init__(self, color):
        print(f"A {color} Car instance has been created!")
        
mustang = Car('black') # Prints: A black Car instance has been created!
```

## Inheritance

```python
# Parent class
class Vehicle:
   def __init__(self, color):
       print(f"{color} car instance!")

# Child class
class Car(Vehicle):
   pass

blue_car = Car('blue') # Prints: blue car instance!
red_car = Car('red')   # Prints: red car instance!
```

## Overriding Methods

To override a method in a parent class just create a method with the same name in the child class.
Note that `self` can be used as a reference to the attributes of the instance. 
It's similar to `this` in other languages.

```python
class Book:
   def __init__(self, author, title):
       self.title = title
       self.author = author

   def print_sticker(self):
       print(f"A boring book from {self.author}: {self.title}")

class RomanceNovel(Book):
   def print_sticker(self):
       print(f"A romantic book from {self.author}: {self.title}")

oop_book = Book('Joseph Sabido', 'Object Oriented Programming')
love_book = RomanceNovel('Rebecca Serle', 'In Five Years')
```

