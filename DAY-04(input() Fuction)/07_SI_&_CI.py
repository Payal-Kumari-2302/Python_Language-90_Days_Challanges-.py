#W A P to find out the simple and Coumpound Intrest.

p = int(input("Enter Principle amount in rs:->"))
r = int(input("Enter Rate in percent:->"))
t = int(input("Enter Time in year:->"))
si = (p*r*t)/3
ci = p * ((1 + r/100) ** t - 1)
print("Simple Intrest:",si)
print("compound Intrest:",ci)
