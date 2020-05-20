print("Welcome to the Temperature Conversion App")

f = float(input("What is the given temperature in degrees Fahrenheit: "))

c = (f-32)*5/9
k = c + 273.15

print("Degrees Fahrenheit:\t", f)
print("Degrees Celsius:\t", round(c, 4))
print("Degrees Kelvin:\t\t", round(k, 4))
