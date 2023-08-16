# READ CAREFULLY TO THE END BEFORE YOU START SOLVING THE EXERCISES.
# ----------------------------------------------------------------------------------------------------------------------

# Homework Lesson 6: Lists
# Please use concepts and tools you've learned in previous lessons whenever you can.

# EXAMPLE EXERCISE
# We solved this one for you, to give you an idea of what we expect you to do.

# You have the following team members at work: Eric, Tom, Kelly and You.
# Your company wants to do a lottery, in such a way that those born on an EVEN (divisible by 2) number year receive a
# prize. Create a little program that will ask for the birth years of you and your teammates and builds a list of those
# that will receive a prize. Print the result at the end.

# Create an empty list.
prize_receivers = []

# Take the year input and cast it as int so we can perform a modulus calculation on it later.
birth_year_eric = int(input("Eric's birth year:"))
birth_year_tom = int(input("Tom's birth year:"))
birth_year_kelly = int(input("Kelly's birth year:"))
birth_year_you = int(input("Your birth year:"))

# Figure out if any of the years are multiples of two, by using the modulus operator (%).
# Those that are, are added to the prize_receivers list.
if birth_year_eric % 2 == 0:
    prize_receivers.append("Eric")

if birth_year_tom % 2 == 0:
    prize_receivers.append("Tom")

if birth_year_kelly % 2 == 0:
    prize_receivers.append("Kelly")

if birth_year_you % 2 == 0:
    prize_receivers.append("You")

# Print the result.
print("The following people receive a prize:")
print(prize_receivers)



