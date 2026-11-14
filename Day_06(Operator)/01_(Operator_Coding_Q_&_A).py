#Operators in Python


#AirthMatical / Mathematical Operator
#Operators: +, -, *, /, %, //, **

#Direct Method

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




# Take User input method

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


#Use Mathematical function


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


#Use math module

import math

print(math.pi)
print(math.e)

x = 9.1

print(math.ceil(x))
print(math.floor(x))
print(math.sqrt(25))
print(math.factorial(5))




#2. Assignment Operators
#Operators: =, +=, -=, *=, /=, //=, %=, **=


#A. Direct Method

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

#B. User Input Method

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



# 3. Comparison (Relational) Operators
# Operators: ==, !=, >, <, >=, <=


# A. Direct Method

a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


#B. User Input Method

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater:", a > b)
print("Smaller:", a < b)
print("Greater or Equal:", a >= b)
print("Smaller or Equal:", a <= b)


# 4. Logical Operators
# Operators: and, or, not
# A. Direct Method

a = 10
b = 5

print(a > 5 and b < 10)
print(a > 15 or b < 10)
print(not(a > 5))


#B. User Input Method

a = int(input("Enter a number: "))

print(a > 0 and a < 100)
print(a < 0 or a > 100)
print(not(a > 0))



# 5. Bitwise Operators
# Operators: &, |, ^, ~, <<, >>


# A. Direct Method

a = 10
b = 3

print(a & b)    # AND
print(a | b)    # OR
print(a ^ b)    # XOR
print(~a)       # NOT
print(a << 2)   # Left Shift
print(a >> 2)   # Right Shift


# B. User Input Method


a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)


# 6. Membership Operators
# Operators: in, not in


# A. Direct Method

numbers = [10, 20, 30, 40, 50]

print(20 in numbers)
print(60 in numbers)

print(20 not in numbers)
print(60 not in numbers)


# B. User Input Method

numbers = [10, 20, 30, 40, 50]

a = int(input("Enter a number: "))

print("Present:", a in numbers)
print("Not Present:", a not in numbers)


#String Example

name = "Python Programming"

print("Python" in name)
print("Java" in name)

print("Java" not in name)



# 7. Identity Operators
# Operators: is, is not


# A. Direct Method


a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)

print(a is not b)
print(a is not c)


#B. User Input Method

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

x = a
y = b

print(x is y)
print(x is not y)


#C. None Example

x = None
y = 10

print(x is None)
print(y is None)
print(x is not None)
