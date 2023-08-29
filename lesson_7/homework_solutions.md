### The Red Crayon

```python
colors = ["Blue", "Yellow", "Green", "Red", "Purple", "Orange"]
index = 0

while colors[index] != "Red":
    print(f"Found {colors[index]} crayon. Still looking for Red.")
    index += 1

print("Found the Red crayon!")
```

### Digits Only!

**Part One**

```python
my_string = 's0m3 str1ng w1th numb3r5'
numbers = '1234567890'

for character in my_string:
    if character in numbers:
        print(character)
```

**Part Two**
```python
my_string = 's0m3 str1ng w1th numb3r5'
numbers = '1234567890'

for character in my_string:
    if character in numbers:
        print(character)
        # Just add a break here!
        break
```

### Vowel Counter

```python
quote = "Life is like riding a bicycle. To keep your balance, you MUST keep moving."
vowel_count = 0

for char in quote:
    # 'A' and 'a' are different in python, so we include both upper and lowercase
    # vowels in our comparison string to account for this difference.
    if char in 'aeiouAEIOU':
        vowel_count += 1

print(f"The number of vowels in the quote is: {vowel_count}")
```

### Filename Space Remover
```python
flawed_file_name = "My Summer Photos 2023"
fixed_file_name = ""

for char in flawed_file_name:
    if char != " ":
        fixed_file_name += char

print(f"The fixed file name is: {fixed_file_name}")
```

### Sum of all Digits
```python
mixed_string = "abc123xyz456"
digits = "0123456789"
found_digits = []

for char in mixed_string:
    if char in digits:
        found_digits.append(int(char))

print(f"The total sum of numbers in the string is: {sum(found_digits)}")
```

### Email Checker

```python
email_addresses = ['john.doe@example.com', 'jane.doe@work.com', 'invalid.email', 'missing+symbol.com']
valid_emails = []

for email in email_addresses:
    if "@" in email:
        valid_emails.append(email)

print("Valid email addresses are:", valid_emails)
```

### Password Strength Checker

```python
passwords = ['Passw0rd', 'hello', 'strongPass1', 'weak']
strong_password_count = 0

for password in passwords:
    if len(password) >= 8:
        strong_password_count += 1

print(f"Number of strong passwords: {strong_password_count}")
```