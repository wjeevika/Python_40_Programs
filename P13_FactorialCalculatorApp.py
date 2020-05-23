import math as m

print("Welcome to the Factorial Calculator App\n")

n = int(input("What number would you like to compute the factorial of? "))

print(f"{n}! = ", end="")       # to print the procedure of factorial
for i in range(1,n):
    print(i,end="*")
print(n)    # to print last no. of the procedure

f = m.factorial(n)      # using library
print("Here is the result from the math library:")
print(f"The factorial of {n} is {f}!")

print("\nHere is the result from my own algorithm:")
f = 1
for i in range(1,n+1):      # our algorithm
    f *= i

print(f"The factorial of {n} is {f}!")    

print(f"\nIt is shown twice that {n}! = {f} (with excitement)")

