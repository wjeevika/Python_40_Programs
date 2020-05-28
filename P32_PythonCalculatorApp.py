def add(a, b):
    r = round(a+b, 4)
    print(f"The sum of {a} and {b} is {r}")
    s = f'{a} + {b} = {r}'
    return s

def subtract(a, b):
    r = round(a-b,4)
    print(f"The difference of {a} and {b} is {r}")
    s = f'{a} - {b} = {r}'
    return s

def multiply(a, b):
    r = round(a*b, 4)
    print(f"The product of {a} and {b} is {r}")
    s = f'{a} * {b} = {r}'
    return s

def divide(a, b):
    try:
        r = round(a/b, 4)
        print(f"The quotient of {a} and {b} is {r}")
        s = f'{a}/{b} = {r}'
        return s
    except ZeroDivisionError:   # if second number is zero
        print("You cannot divide by zero.")
        return 'DIV ERROR'

def exponent(a, b):
    r = round(a**b, 4)
    print(f"The result of {a} raised to the {b} power is {r}")
    s = f'{a} ** {b} = {r}'
    return s

print("Welcome to The Python Calculator App")
print("Enter two numbers and an operation and the desired operation will be performed.")

running = True
history = []    # to store history of operations performed 

while running:
    a = float(input("\nEnter a number: "))
    b = float(input("Enter a number: "))

    op = input("Enter an operation (addition, subtraction, multiplication, division, or exponentiation): ").lower()

    if op == 'a' or op == 'addition':
        result = add(a, b)

    elif op == 's' or op == 'subtraction':
        result = subtract(a, b)

    elif op == 'm' or op == 'multiplication':
        result = multiply(a, b)

    elif op == 'd' or op == 'division':
        result = divide(a, b)

    elif op == 'e' or op == 'exponentiation':
        result = exponent(a, b)

    else:   
        print("That is not a valid operation. Try again.")
        result = 'OPP ERROR'

    history.append(result)      # adding previous calculations to history
    ch = input("Would you like to run the program again (y/n): ").lower().strip()

    if ch != 'y':
        running = False
        print('\nCalculation Summary:')
        for i in history:   # displaying previous calculations
            print(i)

print("\nThank you for using The Python Calculator App. Goodbye.")