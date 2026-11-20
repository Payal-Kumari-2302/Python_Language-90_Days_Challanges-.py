#String methods



#Q1. lower()
text = "PAYAL"
print(text.lower())

#Q2. upper()
text = "payal"
print(text.upper())

#Q3. capitalize()
text = "payal"
print(text.capitalize())

#Q4.title()
text = "python programming language"
print(text.title())

#Q5. strip()
text = " Payal "
print(text.strip())

#Q6.lstrip()
text = " Payal "
print(text.lstrip())

#Q7 rstrip()
text = " Payal "
print(text.rstrip())

#Q8 replace(old,new)
text = "I like java"
print(text.replace("java","Python"))

#Q9 find()
text = "Payal"
print(text.find("y"))

#Q10_count()
text = "Payal"
print(text.count("l"))


#Q11 startwith()
text = "Payal"
print(text.startswith("P"))
print(text.startswith("p"))
print(text.startswith("M"))
print(text.startswith("m"))

#Q12_endwith()
text = "Payal"
print(text.endswith("l"))
print(text.endswith("L"))
print(text.endswith("j"))
print(text.endswith("J"))

#Q13_split()
text = "Payal Kumari Jaiswal"
print(text.split())

#Q14_join()
text = "Payal", "Kumari","Jaiswal"
print(" ".join(text))

#Q15 isalpha()
text = "Payal"
print(text.isalpha())

#Q16 isdigit
text = "123"
print(text.isdigit())

#Q17_isanum
text = "Payal2302"
print(text.isalnum())

#Q18_swapcase
text = "Payal"
print(text.swapcase())

#Q19_index()
text = "Payal"
print(text.index("y"))

#Q20_isnumeric
text = "Payal2302"
print(text.isnumeric())


#Q21_isspace()
text = "Payal"
print(text.isspace())

text = " "
print(text.isspace())

#Q22_islower  
text = "payal"
print(text.islower())

#Q23_isupper
text = "PAYAl"
print(text.isupper())

#Extra
text = "pAyaL"
print(text.islower())
print(text.isupper())


#24_istitle
text ="Payal Kumari Jaiswal"
print(text.istitle())

text ="Payal kumari Jaiswal"
print(text.istitle())

#Q25_rfind()
text = "Payal Kumari Jaiswal"
print(text.rfind("Jaiswal"))


#Q26_zfill()
text = "25"
print(text.zfill(5))

#Q27_Partition
text = "PYthon is easy"
print(text.partition("is"))

print(text.partition("easy"))
