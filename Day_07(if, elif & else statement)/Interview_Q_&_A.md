# Python – Conditional Statements Interview Questions

## 1. What is an `if` statement?

**Definition:** Executes a block of code when a condition is `True`.

**Real-World Example:** If your age is 18 or above, you can vote.

## 2. What is an `if-else` statement?

**Definition:** Executes one block if the condition is `True`, otherwise executes another block.

**Real-World Example:** Correct password → Login successful; otherwise → Login failed.

## 3. What is an `if-elif-else` statement?

**Definition:** Checks multiple conditions one by one and executes the first matching block.

**Real-World Example:** Assigning grades based on marks.

## 4. What is a nested `if` statement?

**Definition:** An `if` statement inside another `if` statement.

**Real-World Example:** If a user is logged in, check whether they are an admin.

## 5. What happens if all conditions are False?

**Answer:** The `else` block executes if present. Otherwise, Python skips the conditional block.

## 6. Can we use multiple `elif` statements?

**Answer:** Yes, we can use multiple `elif` statements.

## 7. Is `else` compulsory in Python?

**Answer:** No, `else` is optional.

## 8. Can we use `if` without `else`?

**Answer:** Yes, an `if` statement can be used independently.

## 9. Can we use `elif` without `if`?

**Answer:** No, `elif` must follow an `if` statement.


## Difference Between `if`, `if-else` and `if-elif-else`

| Basis | `if` | `if-else` | `if-elif-else` |
|---|---|---|---|
| 1. Purpose | Checks a single condition. | Checks a condition with two possible outcomes. | Checks multiple conditions. |
| 2. Conditions | Uses one condition. | Uses one condition. | Uses multiple conditions. |
| 3. Execution | Executes code only when the condition is True. | Executes either the `if` or `else` block. | Executes the first block whose condition is True. |
| 4. False Condition | Skips the block if the condition is False. | Executes the `else` block. | Checks the next `elif` condition. |
| 5. Else Block | Optional. | Used to handle the False condition. | Optional; handles cases where all conditions are False. |
| 6. Usage | Simple decision-making. | Two-way decision-making. | Multiple-choice decision-making. |

### Real-World Examples

**1. if:** 
If age >= 18 → Eligible to vote.

**2. if-else:**
If password is correct → Login successful; otherwise → Login failed.

**3. if-elif-else:**
- Marks >= 90 → Grade A
- Marks >= 75 → Grade B
- Marks >= 50 → Grade C
- Otherwise → Fail

### Important Interview Point
- `if` checks a condition.
- `if-else` handles two possible outcomes.
- `if-elif-else` handles multiple possible outcomes.
- In an `if-elif-else` chain, only the first matching block executes.
