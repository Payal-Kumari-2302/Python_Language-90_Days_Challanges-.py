# 🐍 PYTHON STRING – INTERVIEW PREPARATION

**Target Audience:** BCA Students & Freshers  
**Target Companies:** TCS, Wipro, Infosys, Accenture, Cognizant, Genpact & Deloitte.

---

# PART 1 – BASIC STRING CONCEPTS

### 1. What is a String in Python?
**Definition:** A string is a sequence of characters enclosed in quotes.

**Example:**
```python
name = "Payal"
```
**Real-World Example:** Storing a user's name in a registration form.

### 2. Why are strings immutable in Python?
**Definition:** Strings are immutable because their characters cannot be changed after creation.

**Example:**
```python
name = "Python"
# name[0] = "J"  # TypeError
```
**Real-World Example:** A generated transaction ID should not be accidentally modified.

### 3. How do you create a string in Python?
**Definition:** Strings can be created using single, double or triple quotes.

**Example:**
```python
a = 'Hello'
b = "Python"
c = """Welcome"""
```
**Real-World Example:** Storing messages, names and descriptions.

### 4. What is string indexing?
**Definition:** Indexing is used to access individual characters using their position.

**Example:**
```python
text = "Python"
print(text[0])  # P
```
**Real-World Example:** Accessing the first letter of a username.

### 5. What is negative indexing?
**Definition:** Negative indexing accesses characters from the end of a string.

**Example:**
```python
text = "Python"
print(text[-1])  # n
```
**Real-World Example:** Accessing the last digit of an order ID.

### 6. What is string slicing?
**Definition:** Slicing extracts a portion of a string using start, stop and step.

**Example:**
```python
text = "Python"
print(text[0:3])  # Pyt
```
**Real-World Example:** Extracting the first four characters of a customer ID.

### 7. What is string concatenation?
**Definition:** Concatenation combines two or more strings using the `+` operator.

**Example:**
```python
first = "Hello"
second = "Payal"
print(first + " " + second)
```
**Output:** `Hello Payal`

**Real-World Example:** Combining first name and last name.

### 8. How do you find the length of a string?
**Definition:** The `len()` function returns the total number of characters in a string, including spaces.

**Example:**
```python
text = "Python"
print(len(text))  # 6
```
**Real-World Example:** Checking the length of a password.

### 9. How do you access the first and last character of a string?
**Definition:** Use index `0` for the first character and `-1` for the last character.

**Example:**
```python
text = "Python"
print(text[0])   # P
print(text[-1])  # n
```
**Real-World Example:** Checking the first and last letters of a name.

### 10. How do you check whether a substring exists in a string?
**Definition:** The `in` operator checks whether a substring exists in another string.

**Example:**
```python
text = "I love Python"
print("Python" in text)  # True
```
**Real-World Example:** Searching for a keyword in a message.

### 11. What is the difference between a string and a list?

**Definition:**
- String: An immutable sequence of characters.
- List: A mutable collection of elements.

**Example:**
```python
text = "Python"
items = ["Python", "Java"]

items[0] = "C++"
```
**Real-World Example:**
- String: Employee name.
- List: Employee names.

### 12. Can a string contain numbers and special characters?
**Definition:** Yes, strings can contain letters, numbers, spaces and special characters.

**Example:**
```python
text = "Payal@123"
```
**Real-World Example:** Storing passwords and email addresses.

### 13. What is an empty string?
**Definition:** An empty string is a string containing zero characters.

**Example:**
```python
text = ""
print(len(text))  # 0
```
**Real-World Example:** An empty form field before the user enters information.

### 14. What is the difference between single, double and triple quotes?
**Definition:** All three can create strings. Triple quotes also support multiline strings.

**Example:**
```python
a = 'Hello'
b = "Hello"
c = """Hello
Welcome"""
```
**Real-World Example:** Using triple quotes to store multiline descriptions.

### 15. How do you traverse a string using a loop?
**Definition:** Traversal means accessing each character of a string one by one.

**Example:**
```python
text = "Python"

for char in text:
    print(char)
```
**Real-World Example:** Checking each character of a password.

---


# PART 2 – IMPORTANT STRING METHODS

| No. | Method | Short Definition | Python Example | Real-World Example |
|---|---|---|---|---|
| 1 | `upper()` ⭐ | Converts all letters to uppercase. | `"hello".upper()` → `HELLO` | Converting names or codes to uppercase. |
| 2 | `lower()` ⭐ | Converts all letters to lowercase. | `"HELLO".lower()` → `hello` | Normalizing email addresses. |
| 3 | `strip()` ⭐ | Removes leading and trailing whitespace. | `" Hi ".strip()` → `Hi` | Removing extra spaces from user input. |
| 4 | `split()` ⭐ | Splits a string into a list. | `"A B".split()` → `['A', 'B']` | Separating a full name into words. |
| 5 | `join()` ⭐ | Joins iterable elements into a string. | `"-".join(["A","B"])` → `A-B` | Combining words into a sentence. |
| 6 | `replace()` ⭐ | Replaces a substring with another substring. | `"cat".replace("c","b")` → `bat` | Replacing old text with new text. |
| 7 | `find()` ⭐ | Returns the first matching position or -1. | `"Python".find("t")` → `2` | Searching for a keyword in a message. |
| 8 | `index()` ⭐ | Returns the first matching position or raises ValueError. | `"Python".index("t")` → `2` | Finding the position of a required character. |
| 9 | `count()` ⭐ | Counts occurrences of a substring. | `"hello".count("l")` → `2` | Counting repeated letters in a username. |
| 10 | `startswith()` | Checks whether a string starts with given text. | `"Python".startswith("Py")` → `True` | Checking a particular prefix in an ID. |
| 11 | `endswith()` | Checks whether a string ends with given text. | `"Python".endswith("on")` → `True` | Checking file extensions like `.pdf`. |
| 12 | `capitalize()` | Capitalizes the first character and lowercases the rest. | `"python".capitalize()` → `Python` | Formatting a person's name. |
| 13 | `title()` | Capitalizes the first character of each word. | `"hello world".title()` → `Hello World` | Formatting headings and names. |
| 14 | `swapcase()` | Changes uppercase to lowercase and vice versa. | `"PyThOn".swapcase()` → `pYtHoN` | Changing the case of text. |
| 15 | `isalpha()` ⭐ | Checks whether all characters are alphabetic. | `"Hello".isalpha()` → `True` | Validating an alphabet-only name field. |
| 16 | `isdigit()` ⭐ | Checks whether all characters are digits. | `"123".isdigit()` → `True` | Validating a numeric OTP. |
| 17 | `isalnum()` ⭐ | Checks whether all characters are letters or digits. | `"ABC123".isalnum()` → `True` | Validating an alphanumeric username. |
| 18 | `isspace()` | Checks whether all characters are whitespace. | `"   ".isspace()` → `True` | Checking whether input contains only spaces. |
| 19 | `center()` | Centers a string within a specified width. | `"Hi".center(6)` → `'  Hi  '` | Center-aligning text in console output. |
| 20 | `lstrip()` / `rstrip()` | Removes leading / trailing whitespace. | `" Hi ".lstrip()` → `Hi ` | Removing unwanted spaces from input. |


---

# PART 3 – OUTPUT-BASED INTERVIEW QUESTIONS

### Q1. What is the output of `"Python"[::-1]`?

```python
print("Python"[::-1])
```
**Output:** `nohtyP`

**Explanation:** Negative step reverses the string.

### Q2. What is the output of `"Programming"[0:5]`?

```python
print("Programming"[0:5])
```
**Output:** `Progr`

**Explanation:** Start index is included, stop index is excluded.

### Q3. What is the output of `"Hello".upper()`?

```python
print("Hello".upper())
```
**Output:** `HELLO`

**Explanation:** Converts all letters to uppercase.

### Q4. What is the output of `"Python".count("o")`?

```python
print("Python".count("o"))
```
**Output:** `1`

**Explanation:** Counts the occurrences of `o`.

### Q5. What is the output of `"Hello World".split()`?

```python
print("Hello World".split())
```
**Output:** `['Hello', 'World']`

**Explanation:** Splits the string using whitespace.

### Q6. What is the output of `"python".capitalize()`?

```python
print("python".capitalize())
```
**Output:** `Python`

**Explanation:** Capitalizes the first character.

### Q7. What is the output of `"Python".find("t")`?

```python
print("Python".find("t"))
```
**Output:** `2`

**Explanation:** Returns the index of the first matching character.

### Q8. What is the output of `"Hello".replace("l", "x")`?

```python
print("Hello".replace("l", "x"))
```
**Output:** `Hexxo`

**Explanation:** Replaces all occurrences of `l` with `x`.

### Q9. What is the output of `"Python".startswith("Py")`?

```python
print("Python".startswith("Py"))
```
**Output:** `True`

**Explanation:** Checks whether the string starts with `Py`.

### Q10. What is the output of `"12345".isdigit()`?

```python
print("12345".isdigit())
```
**Output:** `True`

**Explanation:** All characters are digits.

---


**Target:** Understand every definition, execute every example and practise explaining the output without looking at the solution.
