#5. List (list)
#Q5. Find the second-largest element in a list.

numbers = [10, 20, 40, 30, 50]

unique = sorted(set(numbers))

print("Second Largest:", unique[-2])


Output: Second Largest: 40
