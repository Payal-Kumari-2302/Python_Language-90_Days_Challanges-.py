
## Temperature Conversion Program

#WAP to convert Celsius to Fahrenheit and Fahrenheit to Celsius.**


# Temperature Program

unit = input("Enter temperature unit (C/F): ").lower()
temp = float(input("Enter the temperature: "))

if unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")

elif unit == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")

else:
    print(f"{unit} is an invalid unit of measurement.")
```

#Output 1:

Enter temperature unit (C/F): c
Enter the temperature: 37
The temperature in Fahrenheit is: 98.6°F
```


#Output 2:
```text
Enter temperature unit (C/F): f
Enter the temperature: 98.6
The temperature in Celsius is: 37.0°C
```

#Output 3:

Enter temperature unit (C/F): k
Enter the temperature: 100
k is an invalid unit of measurement.
