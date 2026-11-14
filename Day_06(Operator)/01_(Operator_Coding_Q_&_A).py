# Python Operators

# 1. Arithmetic / Mathematical Operators
**Operators:** `+, -, *, /, %, //, **`

### A. Direct Method
```python
a = 10
b = 3

add = a + b
sub = a - b
mul = a * b
div = a / b
mod = a % b
floor = a // b
power = a ** b

print(add)
print(sub)
print(mul)
print(div)
print(mod)
print(floor)
print(power)
```

### Output
```text
13
7
30
3.3333333333333335
1
3
1000
```

### B. User Input Method
```python
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

add = a + b
sub = a - b
mul = a * b
div = a / b
mod = a % b
floor = a // b
power = a ** b

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
print("Modulus:", mod)
print("Floor Division:", floor)
print("Exponentiation:", power)
```

### Sample Input
```text
Enter 1st Number: 10
Enter 2nd Number: 3
```

### Output
```text
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Modulus: 1
Floor Division: 3
Exponentiation: 1000
```

### C. Mathematical Functions
```python
x = 3.14
y = -4
z = 5

result1 = round(x)
result2 = abs(y)
result3 = pow(4, 3)
result4 = max(x, y, z)
result5 = min(x, y, z)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
```

### Output
```text
3
4
64
5
-4
```

### D. Math Module
```python
import math

print(math.pi)
print(math.e)

x = 9.1

print(math.ceil(x))
print(math.floor(x))
print(math.sqrt(25))
print(math.factorial(5))
```

### Output
```text
3.141592653589793
2.718281828459045
10
9
5.0
120
```

---

# 2. Assignment Operators
**Operators:** `=, +=, -=, *=, /=, //=, %=, **=`

### A. Direct Method
```python
a = 10

a += 5
print(a)

a -= 3
print(a)

a *= 2
print(a)

a /= 4
print(a)

a //= 2
print(a)

a %= 2
print(a)

a **= 3
print(a)
```

### Output
```text
15
12
24
6.0
3.0
1.0
1.0
```

### B. User Input Method
```python
a = int(input("Enter a number: "))

a += 5
print("Addition Assignment:", a)

a -= 2
print("Subtraction Assignment:", a)

a *= 2
print("Multiplication Assignment:", a)

a /= 2
print("Division Assignment:", a)

a //= 2
print("Floor Division Assignment:", a)

a %= 2
print("Modulus Assignment:", a)

a **= 2
print("Exponentiation Assignment:", a)
```

### Sample Input
```text
Enter a number: 10
```

### Output
```text
Addition Assignment: 15
Subtraction Assignment: 13
Multiplication Assignment: 26
Division Assignment: 13.0
Floor Division Assignment: 6.0
Modulus Assignment: 0.0
Exponentiation Assignment: 0.0
```

---

# 3. Comparison (Relational) Operators
**Operators:** `==, !=, >, <, >=, <=`

### A. Direct Method
```python
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

### Output
```text
False
True
True
False
True
False
```

### B. User Input Method
```python
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater:", a > b)
print("Smaller:", a < b)
print("Greater or Equal:", a >= b)
print("Smaller or Equal:", a <= b)
```

### Sample Input
```text
Enter 1st Number: 10
Enter 2nd Number: 5
```

### Output
```text
Equal: False
Not Equal: True
Greater: True
Smaller: False
Greater or Equal: True
Smaller or Equal: False
```

---

# 4. Logical Operators
**Operators:** `and, or, not`

### A. Direct Method
```python
a = 10
b = 5

print(a > 5 and b < 10)
print(a > 15 or b < 10)
print(not(a > 5))
```

### Output
```text
True
True
False
```

### B. User Input Method
```python
a = int(input("Enter a number: "))

print(a > 0 and a < 100)
print(a < 0 or a > 100)
print(not(a > 0))
```

### Sample Input
```text
Enter a number: 10
```

### Output
```text
True
False
False
```

---

# 5. Bitwise Operators
**Operators:** `&, |, ^, ~, <<, >>`

### A. Direct Method
```python
a = 10
b = 3

print(a & b)    # AND
print(a | b)    # OR
print(a ^ b)    # XOR
print(~a)       # NOT
print(a << 2)   # Left Shift
print(a >> 2)   # Right Shift
```

### Output
```text
2
11
9
-11
40
2
```

### B. User Input Method
```python
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)
```

### Sample Input
```text
Enter 1st Number: 10
Enter 2nd Number: 3
```

### Output
```text
AND: 2
OR: 11
XOR: 9
NOT: -11
Left Shift: 40
Right Shift: 2
```

---

# 6. Membership Operators
**Operators:** `in, not in`

### A. Direct Method
```python
numbers = [10, 20, 30, 40, 50]

print(20 in numbers)
print(60 in numbers)

print(20 not in numbers)
print(60 not in numbers)
```

### Output
```text
True
False
False
True
```

### B. User Input Method
```python
numbers = [10, 20, 30, 40, 50]

a = int(input("Enter a number: "))

print("Present:", a in numbers)
print("Not Present:", a not in numbers)
```

### Sample Input
```text
Enter a number: 20
```

### Output
```text
Present: True
Not Present: False
```

### C. String Example
```python
name = "Python Programming"

print("Python" in name)
print("Java" in name)

print("Java" not in name)
```

### Output
```text
True
False
True
```

---

# 7. Identity Operators
**Operators:** `is, is not`

### A. Direct Method
```python
a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)

print(a is not b)
print(a is not c)
```

### Output
```text
True
False
False
True
```

### B. User Input Method
```python
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

x = a
y = b

print(x is y)
print(x is not y)
```

**Note:** Integer identity results can depend on Python implementation and object caching. Use `==` for comparing numerical values.

### C. None Example
```python
x = None
y = 10

print(x is None)
print(y is None)
print(x is not None)
```

### Output
```text
True
False
True


---

# 9. Important Output-Based Interview Questions

| Expression | Output |
|---|---|
| `10 + 3` | `13` |
| `10 - 3` | `7` |
| `10 * 3` | `30` |
| `10 / 3` | `3.3333333333333335` |
| `10 // 3` | `3` |
| `10 % 3` | `1` |
| `2 ** 3` | `8` |
| `10 > 5` | `True` |
| `10 == 5` | `False` |
| `True and False` | `False` |
| `True or False` | `True` |
| `not True` | `False` |
| `10 & 3` | `2` |
| `10 \| 3` | `11` |
| `10 ^ 3` | `9` |
| `~10` | `-11` |
| `10 << 2` | `40` |
| `10 >> 2` | `2` |
| `20 in [10,20,30]` | `True` |
| `40 not in [10,20,30]` | `True` |

---

# 10. Important Mathematical Functions

| Function | Definition | Example |
|---|---|---|
| `round()` | Rounds a number. | `round(3.14) → 3` |
| `abs()` | Returns absolute value. | `abs(-4) → 4` |
| `pow()` | Calculates power. | `pow(2,3) → 8` |
| `max()` | Returns the largest value. | `max(2,5,3) → 5` |
| `min()` | Returns the smallest value. | `min(2,5,3) → 2` |
| `math.sqrt()` | Returns square root. | `math.sqrt(25) → 5.0` |
| `math.factorial()` | Returns factorial. | `math.factorial(5) → 120` |
| `math.ceil()` | Rounds up. | `math.ceil(9.1) → 10` |
| `math.floor()` | Rounds down. | `math.floor(9.1) → 9` |

---

**Placement Preparation:** Arithmetic, Comparison, Logical, Assignment, Bitwise, Membership and Identity operators ke concepts, examples aur output-based questions achhe se practice karo.
