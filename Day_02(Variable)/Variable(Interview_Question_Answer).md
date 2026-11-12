# Variables in Python – Interview Questions & Answers

### Q1. What is a variable in Python?

A variable is a name used to store or refer to a value in Python.

```python
name = "Payal"
age = 21
```

### Q2. How do you declare a variable in Python?

We declare a variable by assigning a value using the assignment operator (`=`).

```python
x = 10
name = "Payal"
```

### Q3. What are the rules for naming variables in Python?

1. A variable name must start with a letter or underscore (`_`).
2. It cannot start with a number.
3. It can contain letters, numbers and underscores.
4. Variable names are case-sensitive.
5. Spaces are not allowed.
6. Python keywords cannot be used as variable names.

### Q4. Is variable declaration required in Python?

No, explicit variable declaration is not required in Python. A variable is created automatically when a value is assigned to it.

### Q5. What is dynamic typing in Python?

Dynamic typing means we do not need to specify the data type of a variable. Python determines its type at runtime.

```python
x = 10
x = "Python"
```

### Q6. Are variable names case-sensitive in Python?

Yes, Python variable names are case-sensitive. Uppercase and lowercase letters are treated differently.

```python
name = "Payal"
Name = "Kumari"
```

### Q7. Can we change the value of a variable?

Yes, we can change the value of a variable by assigning a new value to it.

```python
x = 10
x = 20
```

### Q8. Can a variable store different data types?

Yes, a Python variable can refer to values of different data types.

```python
x = 10
x = "Python"
x = 10.5
```

### Q9. What is variable reassignment?

Variable reassignment means assigning a new value to an existing variable.

```python
x = 10
x = 50
```

### Q10. What is multiple assignment in Python?

Multiple assignment means assigning values to multiple variables in a single statement.

```python
a, b, c = 10, 20, 30
```

### Q11. What is multiple variable assignment with the same value?

It means assigning the same value to multiple variables in a single statement.

```python
a = b = c = 100
```

### Q12. What is the difference between local and global variables?

| Local Variable | Global Variable |
|---|---|
| Declared inside a function. | Declared outside functions. |
| Accessible within its function. | Accessible throughout the module. |
| Usually exists during function execution. | Usually exists while the module is loaded. |

### Q13. What is a constant in Python?

A constant is a value that is intended to remain unchanged throughout a program. Python does not enforce constants.

```python
PI = 3.14
MAX_SIZE = 100
```

### Q14. What is the difference between a variable and a constant?

| Variable | Constant |
|---|---|
| Its value can be changed. | Intended to remain unchanged. |
| Usually written in lowercase. | Usually written in uppercase. |
| Example: `age = 21` | Example: `PI = 3.14` |

### Q15. Can we use Python keywords as variable names?

No, Python keywords cannot be used as variable names because they have special meanings in Python.

```python
if = 10  # Invalid
```

### Q16. Can a variable name start with an underscore?

Yes, a variable name can start with an underscore (`_`).

```python
_name = "Payal"
```

### Q17. Can a variable name start with a number?

No, a variable name cannot start with a number.

```python
1name = "Payal"  # Invalid
name1 = "Payal"  # Valid
```

### Q18. What happens when we assign a new value to an existing variable?

The variable starts referring to the new value. The previous value may become eligible for garbage collection if no references remain.

```python
x = 10
x = 20
print(x)
```

**Output:**
```text
20
```

### Q19. How do you delete a variable in Python?

We can delete a variable using the `del` keyword.

```python
x = 100
del x
```

### Q20. How can you check the type of a variable?

We can use the built-in `type()` function to check the data type of a variable.

```python
x = 10
print(type(x))
```

**Output:**
```text
<class 'int'>
```

### Q21. What is the difference between `=` and `==`?

| `=` | `==` |
|---|---|
| Assignment operator. | Comparison operator. |
| Assigns a value to a variable. | Checks whether two values are equal. |
| Example: `x = 10` | Example: `x == 10` |

### Q22. Can two variables have the same value?

Yes, two or more variables can have the same value.

```python
a = 10
b = 10
```

### Q23. What is variable scope in Python?

Variable scope refers to the region of a program where a variable can be accessed.

Python follows the LEGB rule:

1. Local
2. Enclosing
3. Global
4. Built-in

### Q24. What is the difference between local, global and nonlocal variables?

| Variable | Definition |
|---|---|
| Local | Declared inside a function. |
| Global | Declared at the module level. |
| Nonlocal | Refers to a variable in an enclosing function. |

### Q25. What is the lifetime of a variable in Python?

The lifetime of a variable refers to the period during which its name or object reference exists.

- Local variables generally exist during function execution.
- Global variables generally exist while their module is loaded.
- Object lifetime depends on whether references to the object still exist.
