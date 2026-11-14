# Python Operators – Interview Notes

## 1. Arithmetic Operators

**Definition:** Arithmetic operators are used to perform mathematical operations such as addition, subtraction, multiplication and division.

| Operator | Definition | Example |
|---|---|---|
| `+` Addition | Adds two values. | `5 + 3 = 8` |
| `-` Subtraction | Subtracts one value from another. | `5 - 3 = 2` |
| `*` Multiplication | Multiplies two values. | `5 * 3 = 15` |
| `/` Division | Divides one value by another and returns a float result. | `5 / 2 = 2.5` |
| `//` Floor Division | Returns the quotient rounded down. | `5 // 2 = 2` |
| `%` Modulus | Returns the remainder after division. | `5 % 2 = 1` |
| `**` Exponentiation | Raises a number to the power of another number. | `2 ** 3 = 8` |

## 2. Comparison Operators

**Definition:** Comparison operators are used to compare two values and return a Boolean result (True or False).

| Operator | Definition | Example |
|---|---|---|
| `==` | Checks whether two values are equal. | `5 == 5 → True` |
| `!=` | Checks whether two values are not equal. | `5 != 3 → True` |
| `>` | Checks whether the left value is greater. | `5 > 3 → True` |
| `<` | Checks whether the left value is smaller. | `3 < 5 → True` |
| `>=` | Checks whether the left value is greater than or equal to the right value. | `5 >= 5 → True` |
| `<=` | Checks whether the left value is less than or equal to the right value. | `3 <= 5 → True` |

## 3. Assignment Operators

**Definition:** Assignment operators are used to assign values to variables or update their existing values.

| Operator | Definition | Example |
|---|---|---|
| `=` | Assigns a value to a variable. | `x = 5` |
| `+=` | Adds and assigns the result. | `x += 3` |
| `-=` | Subtracts and assigns the result. | `x -= 3` |
| `*=` | Multiplies and assigns the result. | `x *= 3` |
| `/=` | Divides and assigns the result. | `x /= 3` |
| `//=` | Floor divides and assigns the result. | `x //= 3` |
| `%=` | Finds remainder and assigns the result. | `x %= 3` |
| `**=` | Calculates power and assigns the result. | `x **= 3` |
| `&=` | Performs bitwise AND and assigns. | `x &= 3` |
| `\|=` | Performs bitwise OR and assigns. | `x \|= 3` |
| `^=` | Performs bitwise XOR and assigns. | `x ^= 3` |
| `<<=` | Performs left shift and assigns. | `x <<= 1` |
| `>>=` | Performs right shift and assigns. | `x >>= 1` |

## 4. Logical Operators

**Definition:** Logical operators are used to combine or reverse conditional expressions.

| Operator | Definition | Example |
|---|---|---|
| `and` | Returns True if both conditions are True. | `5 > 3 and 4 > 2 → True` |
| `or` | Returns True if at least one condition is True. | `5 < 3 or 4 > 2 → True` |
| `not` | Reverses the Boolean result. | `not True → False` |

## 5. Bitwise Operators

**Definition:** Bitwise operators perform operations on the binary representation of integer values.

| Operator | Definition | Example |
|---|---|---|
| `&` AND | Returns 1 if both bits are 1. | `5 & 3 = 1` |
| `\|` OR | Returns 1 if at least one bit is 1. | `5 \| 3 = 7` |
| `^` XOR | Returns 1 if the bits are different. | `5 ^ 3 = 6` |
| `~` NOT | Inverts all bits. | `~5 = -6` |
| `<<` Left Shift | Shifts bits towards the left. | `5 << 1 = 10` |
| `>>` Right Shift | Shifts bits towards the right. | `5 >> 1 = 2` |

## 6. Membership Operators

**Definition:** Membership operators check whether a value exists in a sequence or collection.

| Operator | Definition | Example |
|---|---|---|
| `in` | Returns True if a value is present. | `2 in [1,2,3] → True` |
| `not in` | Returns True if a value is absent. | `4 not in [1,2,3] → True` |

## 7. Identity Operators

**Definition:** Identity operators check whether two variables refer to the same object in memory.

| Operator | Definition | Example |
|---|---|---|
| `is` | Returns True if both variables refer to the same object. | `a is b` |
| `is not` | Returns True if both variables refer to different objects. | `a is not b` |

## 8. Conditional (Ternary) Expression

**Definition:** A conditional expression evaluates a condition and returns one of two values.

| Operator | Definition | Example |
|---|---|---|
| `if-else` | Selects a value based on a condition. | `result = "Pass" if marks >= 40 else "Fail"` |



## ⭐ Important Conceptual Questions

**Q1. Difference between `is` and `==`?**
- `==` – Compares values.
- `is` – Compares object identity.

**Q2. Difference between `/` and `//`?**
- `/` – Performs normal division.
- `//` – Performs floor division.

**Q3. Difference between `and` and `or`?**
- `and` – True if both conditions are True.
- `or` – True if at least one condition is True.

**Q4. Difference between unary and binary operators?**
- Unary – Works on one operand.
- Binary – Works on two operands.

**Q5. What is operator precedence?**  
It defines the priority of operators.

**Q6. What is operator associativity?**  
It defines the evaluation direction of operators with the same precedence.

**Q7. Does Python support `++` and `--`?**  
No, Python uses `+= 1` and `-= 1`.

**Q8. What is short-circuit evaluation?**  
It stops evaluating a logical expression when the result is already determined.

