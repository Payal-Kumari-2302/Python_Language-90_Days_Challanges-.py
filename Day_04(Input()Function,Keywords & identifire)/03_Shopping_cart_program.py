#Exercise_2 Shopping cart program


item = input("What items would you like to buy?:")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(total)

print(f"You have bought {quantity} * {item} /s")
print(f"Your total is : ${total}")
