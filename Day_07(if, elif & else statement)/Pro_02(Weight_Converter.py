#Python Weight converter Program

weight = float(input("Enter your weight:-"))
unit = input("Kilograms of pounds? (k or L):")

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"your weight is : {round(weight,1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."
    print(f"your weight is : {round(weight,1)} {unit}")
else:
    print(f" {unit} was not valid")


    
