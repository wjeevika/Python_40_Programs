import math as m

print("Welcome to the Right Triangle Solver App\n")

f = float(input("What is the first leg of the triangle: "))
s = float(input("What is the second leg of the triangle: "))

h = round(m.sqrt(f**2 + s**2), 3)
a = round(0.5*f*s, 3)

print(f"\nFor a triangle with legs of {f} and {s} the hypotenuse is {h}.")

print(f"For a triangle with legs of {f} and {s} the area is {a}.")
