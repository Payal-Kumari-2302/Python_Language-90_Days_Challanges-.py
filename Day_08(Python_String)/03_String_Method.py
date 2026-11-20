
# String Methods


# Q1. lower()
text = "PAYAL"
print(text.lower())

# Output:
# payal


# Q2. upper()
text = "payal"
print(text.upper())

# Output:
# PAYAL


# Q3. capitalize()
text = "payal"
print(text.capitalize())

# Output:
# Payal


# Q4. title()
text = "python programming language"
print(text.title())

# Output:
# Python Programming Language


# Q5. strip()
text = " Payal "
print(text.strip())

# Output:
# Payal


# Q6. lstrip()
text = " Payal "
print(text.lstrip())

# Output:
# Payal 


# Q7. rstrip()
text = " Payal "
print(text.rstrip())

# Output:
#  Payal


# Q8. replace(old, new)
text = "I like java"
print(text.replace("java", "Python"))

# Output:
# I like Python


# Q9. find()
text = "Payal"
print(text.find("y"))

# Output:
# 1


# Q10. count()
text = "Payal"
print(text.count("l"))

# Output:
# 1


# Q11. startswith()
text = "Payal"
print(text.startswith("P"))
print(text.startswith("p"))
print(text.startswith("M"))
print(text.startswith("m"))

# Output:
# True
# False
# False
# False


# Q12. endswith()
text = "Payal"
print(text.endswith("l"))
print(text.endswith("L"))
print(text.endswith("j"))
print(text.endswith("J"))

# Output:
# True
# False
# False
# False


# Q13. split()
text = "Payal Kumari Jaiswal"
print(text.split())

# Output:
# ['Payal', 'Kumari', 'Jaiswal']


# Q14. join()
text = "Payal", "Kumari", "Jaiswal"
print(" ".join(text))

# Output:
# Payal Kumari Jaiswal


# Q15. isalpha()
text = "Payal"
print(text.isalpha())

# Output:
# True


# Q16. isdigit()
text = "123"
print(text.isdigit())

# Output:
# True


# Q17. isalnum()
text = "Payal2302"
print(text.isalnum())

# Output:
# True


# Q18. swapcase()
text = "Payal"
print(text.swapcase())

# Output:
# pAYAL


# Q19. index()
text = "Payal"
print(text.index("y"))

# Output:
# 1


# Q20. isnumeric()
text = "Payal2302"
print(text.isnumeric())

# Output:
# False


# Q21. isspace()
text = "Payal"
print(text.isspace())

text = " "
print(text.isspace())

# Output:
# False
# True


# Q22. islower()
text = "payal"
print(text.islower())

# Output:
# True


# Q23. isupper()
text = "PAYAl"
print(text.isupper())

# Output:
# False


# Extra: islower() and isupper()
text = "pAyaL"
print(text.islower())
print(text.isupper())

# Output:
# False
# False


# Q24. istitle()
text = "Payal Kumari Jaiswal"
print(text.istitle())

text = "Payal kumari Jaiswal"
print(text.istitle())

# Output:
# True
# False


# Q25. rfind()
text = "Payal Kumari Jaiswal"
print(text.rfind("Jaiswal"))

# Output:
# 12


# Q26. zfill()
text = "25"
print(text.zfill(5))

# Output:
# 00025


# Q27. partition()
text = "PYthon is easy"
print(text.partition("is"))

print(text.partition("easy"))


# Q28. isdecimal()
text = "123"
print(text.isdecimal())

# Output:
# True


# Q29. isascii()
text = "Payal123"
print(text.isascii())

# Output:
# True


# Q30. isidentifier()
text = "payal_2302"
print(text.isidentifier())

# Output:
# True


# Q31. removeprefix()
text = "Python Programming"
print(text.removeprefix("Python "))

# Output:
# Programming


# Q32. removesuffix()
text = "Payal.pdf"
print(text.removesuffix(".pdf"))

# Output:
# Payal


# Q33. center()
text = "Payal"
print(text.center(11, "*"))

# Output:
# ***Payal***


# Q34. ljust()
text = "Payal"
print(text.ljust(10, "*"))

# Output:
# Payal*****


# Q35. rjust()
text = "Payal"
print(text.rjust(10, "*"))

# Output:
# *****Payal


# Q36. expandtabs()
text = "Python\tProgramming"
print(text.expandtabs(4))

# Output:
# Python  Programming


# Q37. rindex()
text = "Python Programming"
print(text.rindex("P"))

# Output:
# 7


# Q38. rpartition()
text = "Python is easy"
print(text.rpartition("is"))

# Output:
# ('Python ', 'is', ' easy')


# Q39. splitlines()
text = "Python\nJava\nC++"
print(text.splitlines())

# Output:
# ['Python', 'Java', 'C++']


