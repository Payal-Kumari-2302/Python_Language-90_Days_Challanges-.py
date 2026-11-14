#W.A.P to accept radious of circle display area,diameter and circumference of a circle.

import math
r = int(input("Accept radious of circle in cm:->"))
area = 2 * math.pi * r
diameter = 2 * r
circumference = 2 * r * float(22/7)
print("Area of circle:",area)
print("Diameter of circle:",diameter)
print("Circumference of circle",circumference)


#Method_2

import math
r = float(input("Accept radious of circle in cm:->"))
area = math.pi * pow(r,2)                        #area = float(22/7) * r *r
diameter = 2 * r
circumference =  2 * math.pi * r    #circumference = 2 * r * float(22/7)
print(f"Area of circle: {round(area,2)} cm square")
print(f"Diameter of circle: {diameter}")
print(f"Circumference of circle: {round(circumference,2)} cm")
