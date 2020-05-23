import cmath as cm      
# module for performing tasks on complex numbers

print("Welcome to the Quadratic Equation Solver App.\n")

print("A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.\n")

n = int(input("How many equations would you like to solve today: "))

for i in range(n):
    print(f"\nSolving equation #{i+1}")     # displays no. of equation solving
    print("---------------------------------------------------------------\n")

    a = float(input("Please enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))

    print(f"\nThe solutions to {a}x^2 + {b}x + {c} = 0 are:")
    d = b**2 - 4*a*c
    x1 = (-b - cm.sqrt(d))/2*a
    x2 = (-b + cm.sqrt(d))/2*a

    print(f"\n\tx1 = {x1}")     # roots x1 and x2
    print(f"\tx2 = {x2}")

print("\nThank you for using the Quadratic Equation Solver App. Goodbye.")