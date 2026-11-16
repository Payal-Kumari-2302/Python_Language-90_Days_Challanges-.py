#if-  Do some code only if some confition is true else do something else


age =int(input("Enter your age:->"))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


#Second_ example

num = int(input("Enter any number:->"))
if  num >0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#3rd Example

operator = input("Enter an operator(+,-,*,/)")
num1 = float(input("Enter 1st number:-"))
num2 = float(input("Enter 2nd number:-"))

if operator =="+":
    result = num1 + num2
    print(round(num1+num2))
elif operator == "-":
    result = num1 - num2
    print(round(num1-num2))
elif operator == "*":
    result = num1 * num2
    print(round(num1 * num2))
elif operator == "/":
    result = num1 / num2
    print(round(num1/num2))
elif operator == "%":
    result = num1 % num2
    print(round(num1 % num2))
elif operator == "//":
    result = num1 // num2
    print(round(num1 //num2))
else:
    print(f"{operator} is not valid operator")
