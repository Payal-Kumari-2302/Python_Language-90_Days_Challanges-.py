# Day 04 – Python Basics

**Topics:** Input Function, Keywords, Identifiers & Constants

## 1. Input Function

**Definition:** The `input()` function is used to take data from the user.

**Example:**
```python
name = input("Enter name: ")
print(name)
```

**Important:** `input()` always returns data as a string (`str`).

## 2. Keywords

**Definition:** Keywords are reserved words that have predefined meanings in Python.

### 35 Hard Keywords (Python 3.14)

| No. | Keyword | No. | Keyword |
|---:|---|---:|---|
| 1 | False | 19 | if |
| 2 | None | 20 | import |
| 3 | True | 21 | in |
| 4 | and | 22 | is |
| 5 | as | 23 | lambda |
| 6 | assert | 24 | nonlocal |
| 7 | async | 25 | not |
| 8 | await | 26 | or |
| 9 | break | 27 | pass |
| 10 | class | 28 | raise |
| 11 | continue | 29 | return |
| 12 | def | 30 | try |
| 13 | del | 31 | while |
| 14 | elif | 32 | with |
| 15 | else | 33 | yield |
| 16 | except | 34 | finally |
| 17 | for | 35 | from |
| 18 | global | | |

### 4 Soft Keywords

| No. | Soft Keyword | Use |
|---:|---|---|
| 1 | match | Pattern matching |
| 2 | case | Pattern matching |
| 3 | _ | Wildcard in pattern matching |
| 4 | type | Type alias declaration |

**Example:**
```python
age = 18

if age >= 18:
    print("Eligible")
```

Here, `if` is a keyword.

**Important:** Hard keywords cannot be used as identifiers. Soft keywords have special meanings only in particular contexts.

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
| Must start with a letter or `_` | `name`, `_age` |
| Cannot start with a number | `2name` ❌ |
| Can contain numbers | `name2` |
| Cannot contain spaces | `my name` ❌ |
| Cannot use hard keywords | `class` ❌ |
| Case-sensitive | `age` ≠ `Age` |

## 4. Constants

**Definition:** Constants are values intended to remain unchanged throughout a program.

**Example:**
```python
PI = 3.14159
MAX_SIZE = 100
```

**Important:** Python does not have a built-in keyword for declaring constants. Uppercase naming is a convention.

## 5. Important Differences

| Keyword | Identifier | Constant |
|---|---|---|
| Reserved word | User-defined name | Value intended to remain unchanged |
| Predefined meaning | Names program elements | Represents fixed values |
| Example: `if` | Example: `age` | Example: `PI` |

## 6. Practical Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

PI = 3.14

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

## 7. Interview Preparation

### Priority 1 – Must Prepare

1. What is the `input()` function?
2. What is the default return type of `input()`?
3. How do you take integer input?
4. What are keywords in Python?
5. What is the difference between keywords and identifiers?
6. What are the rules for naming identifiers?
7. Are Python identifiers case-sensitive?
8. Does Python support constants?

### Practical Questions

1. Write a program to take two numbers as input and print their sum.
2. Identify valid and invalid identifiers.
3. Write a program using `input()`, `if` and `else`.

---
**Target:** BCA Freshers | TCS Ignite | TCS Smart Hiring | Wipro | Infosys | Accenture
