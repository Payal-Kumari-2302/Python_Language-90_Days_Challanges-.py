# PYTHON INDEXING AND SLICING

## 1. STRING INDEXING

```python
text = "PYTHON"

# Positive Indexing
print(text[0])  # P
print(text[1])  # Y
print(text[2])  # T
print(text[3])  # H
print(text[4])  # O
print(text[5])  # N

# Negative Indexing
print(text[-1])  # N
print(text[-2])  # O
print(text[-3])  # H
print(text[-4])  # T
print(text[-5])  # Y
print(text[-6])  # P

# First and Last Character
print(text[0])   # P
print(text[-1])  # N

# Middle Character
print(text[len(text)//2])  # H
```

**Output:**
```text
P
Y
T
H
O
N
N
O
H
T
Y
P
P
N
H
```

## 2. STRING SLICING (START : STOP)

```python
text = "PYTHON"

print(text[0:3])
print(text[1:4])
print(text[2:5])
print(text[0:6])

# Default Start
print(text[:3])

# Default Stop
print(text[2:])

# Complete String
print(text[:])
```

**Output:**
```text
PYT
YTH
THO
PYTHON
PYT
THON
PYTHON
```

## 3. SLICING WITH STEP

```python
text = "PYTHON"

print(text[0:6:1])
print(text[0:6:2])
print(text[0:6:3])

# Default Start and Stop
print(text[::2])
print(text[1::2])

# Reverse String
print(text[::-1])
print(text[::-2])
```

**Output:**
```text
PYTHON
PTO
PH
PTO
YHN
NOHTYP
NHY
```

## 4. NEGATIVE INDEXING WITH SLICING

```python
text = "PYTHON"

print(text[-5:-1])
print(text[-4:-1])
print(text[-3:])
print(text[:-2])

# Reverse using Negative Index
print(text[-1:-7:-1])
```

**Output:**
```text
YTHO
THO
HON
PYTH
NOHTYP
```

## 5. LIST INDEXING AND SLICING

```python
numbers = [10, 20, 30, 40, 50, 60]

# Positive Indexing
print(numbers[0])
print(numbers[2])

# Negative Indexing
print(numbers[-1])
print(numbers[-2])

# Slicing
print(numbers[0:3])
print(numbers[1:4])
print(numbers[:4])
print(numbers[2:])
print(numbers[:])

# Step
print(numbers[::2])
print(numbers[1::2])

# Reverse List
print(numbers[::-1])
```

**Output:**
```text
10
30
60
50
[10, 20, 30]
[20, 30, 40]
[10, 20, 30, 40]
[30, 40, 50, 60]
[10, 20, 30, 40, 50, 60]
[10, 30, 50]
[20, 40, 60]
[60, 50, 40, 30, 20, 10]
```

## 6. TUPLE INDEXING AND SLICING

```python
fruits = ("Apple", "Banana", "Mango", "Orange")

# Positive Indexing
print(fruits[0])
print(fruits[2])

# Negative Indexing
print(fruits[-1])
print(fruits[-2])

# Slicing
print(fruits[0:2])
print(fruits[1:])
print(fruits[:3])

# Step
print(fruits[::2])

# Reverse Tuple
print(fruits[::-1])
```

**Output:**
```text
Apple
Mango
Orange
Mango
('Apple', 'Banana')
('Banana', 'Mango', 'Orange')
('Apple', 'Banana', 'Mango')
('Apple', 'Mango')
('Orange', 'Mango', 'Banana', 'Apple')
```

## 7. INDEX ERROR EXAMPLE

```python
text = "PYTHON"

# print(text[10])
```

**Output:**
```text
IndexError: string index out of range
```

## 8. STRING IMMUTABILITY

```python
text = "PYTHON"

text[0] = "J"
print(text)
```

**Output:**
```text
TypeError: 'str' object does not support item assignment
```

---




