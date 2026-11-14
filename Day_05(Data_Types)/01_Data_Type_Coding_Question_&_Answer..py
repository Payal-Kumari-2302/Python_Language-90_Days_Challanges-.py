# Python Data Types – Coding Questions with Solutions

## 1. Integer (`int`)

**Q1. Find the sum of digits of an integer.**

```python
num = 1234
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum:", total)
```
**Output:**
```text
Sum: 10
```

## 2. Float (`float`)

**Q2. Calculate the average of three floating-point numbers.**

```python
a = 10.5
b = 20.5
c = 30.5

avg = (a + b + c) / 3

print("Average:", avg)
```
**Output:**
```text
Average: 20.5
```

## 3. Complex (`complex`)

**Q3. Add two complex numbers.**

```python
a = 2 + 3j
b = 4 + 5j

result = a + b

print(result)
```
**Output:**
```text
(6+8j)
```

## 4. String (`str`)

**Q4. Check whether a string is a palindrome.**

```python
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```
**Output:**
```text
Palindrome
```

## 5. List (`list`)

**Q5. Find the second-largest element in a list.**

```python
numbers = [10, 20, 40, 30, 50]

unique = sorted(set(numbers))

print("Second Largest:", unique[-2])
```
**Output:**
```text
Second Largest: 40
```

## 6. Tuple (`tuple`)

**Q6. Find the maximum and minimum elements in a tuple.**

```python
numbers = (10, 20, 5, 40, 30)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
```
**Output:**
```text
Maximum: 40
Minimum: 5
```

## 7. Set (`set`)

**Q7. Find common elements between two sets.**

```python
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print(a.intersection(b))
```
**Output:**
```text
{30, 40}
```

## 8. Dictionary (`dict`)

**Q8. Count the frequency of each character in a string.**

```python
text = "hello"
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
```
**Output:**
```text
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

## 9. Range (`range`)

**Q9. Calculate the sum of numbers from 1 to 10.**

```python
total = 0

for i in range(1, 11):
    total += i

print("Sum:", total)
```
**Output:**
```text
Sum: 55
```

## 10. Boolean (`bool`)

**Q10. Check whether a number is even or odd using a Boolean variable.**

```python
num = 10

is_even = (num % 2 == 0)

print(is_even)
```
**Output:**
```text
True
```

## 11. NoneType (`None`)

**Q11. Check whether a variable contains None.**

```python
value = None

if value is None:
    print("Value is None")
else:
    print("Value is not None")
```
**Output:**
```text
Value is None
```

## 12. Frozenset (`frozenset`)

**Q12. Create a frozenset and check whether an element exists.**

```python
numbers = frozenset([10, 20, 30, 40])

print(20 in numbers)
```
**Output:**
```text
True
```
