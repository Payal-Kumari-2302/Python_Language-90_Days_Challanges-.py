## 1. Type Casting

### Q1. What is type casting in Python?

Type casting is the process of converting one data type into another data type.

**Example:**
```python
x = "10"
y = int(x)

print(y)
print(type(y))
```

**Output:**
```text
10
<class 'int'>
```

### Q2. What are the different types of type casting?

There are two types of type casting in Python:

1. Implicit Type Casting
2. Explicit Type Casting

### Q3. What is implicit type casting?

Implicit type casting is the automatic conversion of one data type into another by Python.

**Example:**
```python
a = 10
b = 2.5

c = a + b

print(c)
print(type(c))
```

**Output:**
```text
12.5
<class 'float'>
```

### Q4. What is explicit type casting?

Explicit type casting is the manual conversion of one data type into another using built-in functions.

**Example:**
```python
x = "100"
y = int(x)

print(y)
print(type(y))
```

**Output:**
```text
100
<class 'int'>
```

### Q5. What is the difference between implicit and explicit type casting?

| Implicit Type Casting | Explicit Type Casting |
|---|---|
| Automatically performed by Python. | Manually performed by the programmer. |
| No conversion function is required. | Built-in conversion functions are used. |
| Usually converts compatible types. | Converts values when the conversion is valid. |
| Example: `10 + 2.5` | Example: `int("10")` |

### Q6. Which functions are used for type casting in Python?

Python provides several built-in functions for type casting:

| Function | Purpose | Example |
|---|---|---|
| `int()` | Converts into integer. | `int("10")` |
| `float()` | Converts into float. | `float("10.5")` |
| `str()` | Converts into string. | `str(100)` |
| `bool()` | Converts into boolean. | `bool(1)` |
| `list()` | Converts into list. | `list("ABC")` |
| `tuple()` | Converts into tuple. | `tuple([1, 2])` |
| `set()` | Converts into set. | `set([1, 2])` |
| `dict()` | Creates a dictionary from suitable key-value pairs. | `dict([("a", 1)])` |
| `complex()` | Converts into complex number. | `complex(10)` |
| `ord()` | Returns Unicode code point of a character. | `ord("A")` |
| `chr()` | Converts Unicode code point into a character. | `chr(65)` |
