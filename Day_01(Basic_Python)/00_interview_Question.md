# 1. Python Fundamentals – Interview Questions & Answers

### Q1. What is Python?

**Answer:** Python is a high-level, interpreted, general-purpose programming language known for its simple syntax.

**Example:**
```python
print("Hello, World!")
```

### Q2. Who developed Python?

**Answer:** Python was developed by Guido van Rossum and first released in 1991.

**Example:** Python is used by companies like Google, Netflix and Instagram.

### Q3. Why is Python called an interpreted language?

**Answer:** Python is called an interpreted language because its code is executed by the Python interpreter.

**Example:**
```python
print("Hello")
print("Welcome to Python")
```

### Q4. What are the main features of Python?

**Answer:** The main features of Python are:

- Easy to learn
- Simple syntax
- Interpreted
- Object-oriented
- Dynamically typed
- Portable
- Open-source

**Example:**
```python
x = 10
name = "Payal"

print(x)
print(name)
```

### Q5. What are the advantages and Disadvantages of Python?

**Answer:**
## - Advantages :-
- Easy to read and write.
- Requires fewer lines of code.
- Provides large library support.
- Free and open-source.
- Supports multiple programming paradigms.

## - Disadvantages :-
- Python is slower than languages like C and C++ and consumes more memory. It is also less suitable for mobile app development and low-level programming.

**Example:**
```python
a = 10
b = 20

print(a + b)
```

### Q6. What are the limitations of Python?

**Answer:**

- Slower than many compiled languages.
- Can consume more memory.
- Not ideal for some mobile applications.
- Dynamic typing can cause runtime errors.

**Example:**
```python
a = 10
b = "20"

print(a + b)
```
**Output:** TypeError

### Q7. Is Python a compiled or interpreted language?

**Answer:** Python is generally known as an interpreted language. In CPython, source code is first compiled into bytecode and then executed by the Python Virtual Machine.

**Example:**
```python
print("Hello Python")
```

### Q8. What is the difference between Python 2 and Python 3?

**Answer:**

| Python 2 | Python 3 |
|---|---|
| Released in 2000 | Released in 2008 |
| `print "Hello"` | `print("Hello")` |
| `5 / 2` gives 2 | `5 / 2` gives 2.5 |
| No longer supported | Actively maintained |

**Example:**

Python 2:
```python
print "Hello World"
```

Python 3:
```python
print("Hello World")
```

### Q9. What is an IDE?

**Answer:** IDE stands for Integrated Development Environment. It is software used to write, execute and debug programs.

**Example:** Visual Studio Code is used to write and run Python programs.

### Q10. Name some popular Python IDEs.

**Answer:**

1. PyCharm
2. Visual Studio Code
3. IDLE
4. Spyder
5. Jupyter Notebook

**Example:** We can write and execute Python programs using VS Code.


# 11 What is Compiler and  Interpreter

## 1. Compiler

**Definition:** A compiler translates the entire source code into machine code before executing the program.

**Examples:** C, C++.

**Real-World Example:** Like translating an entire book into another language before reading it.


## 2. Interpreter

**Definition:** An interpreter translates and executes source code statement by statement (or in smaller units).

**Examples:** Python, JavaScript.

**Real-World Example:** Like translating a book sentence by sentence while reading it.

## 3. Difference Between Compiler and Interpreter

| Basis | Compiler | Interpreter |
|---|---|---|
| Translation | Translates the entire program before execution. | Translates and executes code in smaller units. |
| Execution Speed | Generally faster. | Generally slower. |
| Error Detection | Reports errors during compilation. | Reports errors during execution. |
| Output | Often generates an executable file. | Generally executes instructions without creating a standalone executable. |
| Memory | May require more memory for generated code. | Depends on the interpreter and execution environment. |
| Examples | C, C++ | Python, JavaScript |

## 4. How Does Python Work?

Python is commonly known as an interpreted language.

**Python Execution Process:**

`Python Source Code (.py) → Bytecode (.pyc) → Python Virtual Machine (PVM) → Output`

- **Source Code:** Code written by the programmer.
- **Bytecode:** An intermediate representation of Python code.
- **PVM:** Executes Python bytecode.
- **Output:** Displays the program's result.

**Important:** Python (CPython) first compiles source code into bytecode, then the Python Virtual Machine executes it.

