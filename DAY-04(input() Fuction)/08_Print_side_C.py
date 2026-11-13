#W. A.P to accept side a and side b and print side c

import math
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b,2))
print(f"Side c = {c}")
