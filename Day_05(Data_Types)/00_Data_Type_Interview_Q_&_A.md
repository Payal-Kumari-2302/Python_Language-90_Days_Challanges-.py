# Python Data Types – Important Interview Questions & Answers

**Target Companies:** TCS, TCS Ignite, Wipro, Infosys, Accenture, Cognizant, Deloitte & Other IT Companies.

**Target Audience:** BCA Students & Freshers  
**Primary Programming Language:** Python

## 🔴 Priority 1 – Most Important Questions

### 1. What is a Data Type?
A data type defines the type of value a variable can store.

### 2. What are the different types of data types in Python?
Python has 7 categories of built-in data types:

1. Numeric – `int`, `float`, `complex`
2. Sequence – `str`, `list`, `tuple`, `range`
3. Mapping – `dict`
4. Set – `set`, `frozenset`
5. Boolean – `bool`
6. Binary – `bytes`, `bytearray`, `memoryview`
7. None – `NoneType`

### 3. What is an Integer?
An integer (`int`) represents whole numbers without decimal points.

Example: `10, 20, -5`

### 4. What is a Float?
A float (`float`) represents numbers with decimal points.

Example: `10.5, 3.14, -2.5`

### 5. What is a Complex Data Type?
A complex number contains real and imaginary parts.

Example: `3 + 5j`

### 6. What is a String?
A string (`str`) is a sequence of characters enclosed in quotes.

Example: `"Payal"`

### 7. What is a List?
A list is an ordered, mutable collection that allows duplicate values.

Example: `[10, 20, 30]`

### 8. What is a Tuple?
A tuple is an ordered, immutable collection that allows duplicate values.

Example: `(10, 20, 30)`

### 9. What is a Set?
A set is an unordered collection of unique elements.

Example: `{10, 20, 30}`

### 10. What is a Dictionary?
A dictionary stores data in key-value pairs.

Example: `{"name": "Payal", "age": 22}`

### 11. What is a Boolean Data Type?
Boolean (`bool`) represents two values: `True` and `False`.

### 12. What is NoneType?
NoneType represents the absence of a value.

Example: `x = None`

### 13. What is a Range Data Type?
Range represents a sequence of numbers, commonly used in loops.

Example: `range(1, 5)`

### 14. What are Binary Data Types?
Binary data types are used to handle binary data.

- `bytes` – Immutable binary data.
- `bytearray` – Mutable binary data.
- `memoryview` – Provides access to memory of binary objects without copying.

### 15. What is Dynamic Typing?
Python is dynamically typed because variables do not require explicit type declarations.

### 16. How can we check the data type of a variable?
Using the `type()` function.

Example:
```python
x = 10
print(type(x))
```

Output: `<class 'int'>`

---

## ⭐ Priority 2 – Important Conceptual Questions

### 17. What is the difference between Mutable and Immutable Data Types?

- Mutable: Values can be changed after creation.
- Immutable: Values cannot be changed after creation.



### 18. What is the difference between List and Tuple?

| List | Tuple |
|---|---|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Allows duplicates | Allows duplicates |
| Supports modification | Does not support modification |

### 19. What is the difference between List and Set?

| List | Set |
|---|---|
| Ordered | Unordered |
| Allows duplicates | No duplicates |
| Uses `[]` | Uses `{}` |
| Supports indexing | Does not support indexing |

### 20. What is the difference between List and Dictionary?

| List | Dictionary |
|---|---|
| Stores individual elements | Stores key-value pairs |
| Accessed using index | Accessed using keys |
| Uses `[]` | Uses `{}` |

### 21. What is the difference between Set and Dictionary?

| Set | Dictionary |
|---|---|
| Stores unique elements | Stores key-value pairs |
| No duplicate elements | No duplicate keys |
| Uses `{}` | Uses `{}` |

### 22. What is the difference between `type()` and `isinstance()`?

- `type()` returns the exact type of an object.
- `isinstance()` checks whether an object belongs to a particular type or its subclass.

### 23. Can a List contain different data types?
Yes, a list can store multiple data types.

Example:
```python
data = [10, "Hello", 3.5, True]
```

### 24. Can a Dictionary have duplicate keys?
No, dictionary keys must be unique. A duplicate key overwrites its previous value.

### 25. Can a Set contain duplicate values?
No, sets automatically remove duplicate elements.

### 26. Can a Tuple contain duplicate values?
Yes, tuples allow duplicate values.


```

---

## ⭐ Priority 3 – Output-Based Interview Questions

### Q29. What is the output?
```python
x = 10
print(type(x))
```
**Answer:** `<class 'int'>`

### Q30. What is the output?
```python
x = [10, 20, 30]
x[0] = 100
print(x)
```
**Answer:** `[100, 20, 30]`

### Q31. What is the output?
```python
x = {10, 20, 20, 30}
print(x)
```
**Answer:** `{10, 20, 30}`

### Q32. What is the output?
```python
x = (10, 20, 30)
print(type(x))
```
**Answer:** `<class 'tuple'>`

### Q33. What is the output?
```python
x = None
print(type(x))
```
**Answer:** `<class 'NoneType'>`

### Q34. What is the output?
```python
data = [10, "Python", 3.5, True]
print(len(data))
```
**Answer:** `4`

### Q35. What is the output?
```python
x = {"a": 10, "b": 20}
print(x["a"])
```
**Answer:** `10`

### Q36. What is the output?
```python
x = [10, 20, 30]
y = x
y.append(40)
print(x)
```
**Answer:** `[10, 20, 30, 40]`

### Q37. What is the output?
```python
x = ()
print(type(x))
```
**Answer:** `<class 'tuple'>`

### Q38. What is the output?
```python
x = {}
print(type(x))
```
**Answer:** `<class 'dict'>`

### Q39. What is the output?
```python
x = {1, 2, 3}
print(2 in x)
```
**Answer:** `True`

### Q40. What is the output?
```python
x = "Python"
print(x[0])
```
**Answer:** `P`

---



**Preparation Note:** Focus on understanding the differences between data types, their properties, mutability and output-based questions. These are important Python fundamentals for BCA placement interviews.
