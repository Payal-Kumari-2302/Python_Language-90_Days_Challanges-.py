# Day 04 – Python Basics

**Topics:** Input Function, Keywords, Identifiers & Constants

**Target:** BCA Students | TCS Ignite | TCS Smart Hiring | Wipro | Infosys | Accenture

---

## 1. Input Function

**Definition:** The `input()` function is used to accept data from the user through the keyboard.

**Example:**

```python
name = input("Enter your name: ")
print(name)
```

**Important:** The `input()` function always returns data as a string (`str`).

### Type Conversion with Input

**Integer Input:**

```python
age = int(input("Enter your age: "))
print(age)
```

**Float Input:**

```python
price = float(input("Enter price: "))
print(price)
```

**Multiple Inputs:**

```python
a, b = map(int, input("Enter two numbers: ").split())
print(a + b)
```

---

## 2. Keywords

**Definition:** Keywords are reserved words that have predefined meanings in Python.

### 35 Hard Keywords (Python 3.14)

| No. | Keyword | No. | Keyword |
|---:|---|---:|---|
| 1 | `False` | 19 | `if` |
| 2 | `None` | 20 | `import` |
| 3 | `True` | 21 | `in` |
| 4 | `and` | 22 | `is` |
| 5 | `as` | 23 | `lambda` |
| 6 | `assert` | 24 | `nonlocal` |
| 7 | `async` | 25 | `not` |
| 8 | `await` | 26 | `or` |
| 9 | `break` | 27 | `pass` |
| 10 | `class` | 28 | `raise` |
| 11 | `continue` | 29 | `return` |
| 12 | `def` | 30 | `try` |
| 13 | `del` | 31 | `while` |
| 14 | `elif` | 32 | `with` |
| 15 | `else` | 33 | `yield` |
| 16 | `except` | 34 | `finally` |
| 17 | `for` | 35 | `from` |
| 18 | `global` | | |

### 4 Soft Keywords

| No. | Soft Keyword | Use |
|---:|---|---|
| 1 | `match` | Pattern matching |
| 2 | `case` | Pattern matching |
| 3 | `_` | Wildcard in pattern matching |
| 4 | `type` | Type alias declaration |

**Total: 39 keywords (35 hard + 4 soft).**

**Example:**

```python
age = 18

if age >= 18:
    print("Eligible")
```

Here, `if` is a hard keyword.

**Important Points:**
- Hard keywords cannot be used as identifiers.
- Soft keywords have special meanings only in particular contexts.
- Python keywords are case-sensitive.

---

## 3. Identifiers

**Definition:** Identifiers are names given to variables, functions, classes and other objects.

**Example:**

```python
name = "Payal"
age = 20
```

Here, `name` and `age` are identifiers.

### Rules of Identifiers

| Rule | Example |
|---|---|
| Must start with a letter or underscore | `name`, `_age` |
| Cannot start with a number | `2name` ❌ |
| Can contain numbers | `name2` |
| Cannot contain spaces | `my name` ❌ |
| Cannot be a hard keyword | `class` ❌ |
| Special characters are not allowed except `_` | `my-name` ❌ |
| Identifiers are case-sensitive | `age` ≠ `Age` |

### Case-Sensitive Example

```python
age = 20
Age = 25

print(age)
print(Age)
```

**Output:**

```text
20
25
```

---

## 4. Constants

**Definition:** Constants are values intended to remain unchanged throughout a program.

**Example:**

```python
PI = 3.14159
MAX_SIZE = 100

print(PI)
print(MAX_SIZE)
```

**Important Points:**
- Python does not have a built-in keyword to declare constants.
- Uppercase names are used by convention for constants.
- Python does not strictly prevent their values from being changed.

---

## 5. Important Differences

| Keyword | Identifier | Constant |
|---|---|---|
| Reserved word | User-defined name | Value intended to remain unchanged |
| Predefined meaning | Names program elements | Represents fixed values |
| Example: `if` | Example: `age` | Example: `PI` |

---

# 6. Interview Questions with Short Answers

### Priority 1 – Must Prepare

**Q1. What is the `input()` function?**

Answer: The `input()` function is used to accept data from the user.

**Q2. What is the default return type of `input()`?**

Answer: The default return type is `str` (string).

**Q3. How do you take integer input?**

Answer: By using `int()` with the `input()` function.

Example:

```python
age = int(input("Enter age: "))
```

**Q4. What are keywords in Python?**

Answer: Keywords are reserved words that have predefined meanings in Python.

Example: `if`, `else`, `for`, `while`.

**Q5. What is the difference between keywords and identifiers?**

Answer:
- Keywords are reserved words.
- Identifiers are user-defined names given to variables, functions and classes.

**Q6. What are the rules for naming identifiers?**

Answer: Identifiers must start with a letter or underscore, cannot start with a number, cannot contain spaces and cannot be hard keywords.

**Q7. Are Python identifiers case-sensitive?**

Answer: Yes, Python treats uppercase and lowercase letters as different.

Example: `age` and `Age` are different identifiers.

**Q8. Does Python support constants?**

Answer: Python does not have a built-in constant declaration keyword. Uppercase names are used by convention.

Example: `PI = 3.14`

---

# 7. Practical Interview Questions with Solutions

### Q1. Write a program to take two numbers as input and print their sum.

**Solution:**

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

total = a + b

print("Sum =", total)
```

**Output:**

```text
Enter first number: 10
Enter second number: 20
Sum = 30
```

### Q2. Identify valid and invalid identifiers.

| Identifier | Answer | Reason |
|---|---|---|
| `name` | Valid | Starts with a letter |
| `2name` | Invalid | Starts with a number |
| `_age` | Valid | Starts with underscore |
| `class` | Invalid | Python keyword |
| `total_marks` | Valid | Underscore allowed |
| `my-name` | Invalid | Hyphen not allowed |
| `name2` | Valid | Numbers allowed after first character |
| `my name` | Invalid | Spaces not allowed |
| `Age` | Valid | Valid identifier |
| `@value` | Invalid | Special character not allowed |

### Q3. Write a program using `input()`, `if` and `else`.

**Solution:**

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

**Output 1:**

```text
Enter your age: 20
You are eligible to vote.
```

**Output 2:**

```text
Enter your age: 15
You are not eligible to vote.
```

**Concepts Used:**

| Function/Keyword | Purpose |
|---|---|
| `input()` | Takes user input |
| `int()` | Converts input into integer |
| `if` | Checks a condition |
| `else` | Executes when condition is false |

---

## 8. Important Revision Points

1. `input()` always returns a string.
2. `int()` converts a value into an integer.
3. Python 3.14 has 35 hard keywords and 4 soft keywords.
4. Keywords cannot be used as identifiers.
5. Identifiers are case-sensitive.
6. Identifiers cannot start with numbers.
7. Python does not have a built-in constant declaration keyword.
8. Uppercase naming is the convention for constants.

---

**Day 04 Completed – Python Input Function, Keywords, Identifiers & Constants.**
