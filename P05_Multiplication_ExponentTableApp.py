print("Welcome to the Multiplication/Exponent Table App\n")

name = input("What is your name: ")
n = float(input("What number would you like to work with: "))
s = name.capitalize() + ' Math is cool!'
# string to print the end message

print("\nMultiplication Table For",n,"\n")

for i in range(1,10):   # table from 1 to 9
    m = round(n*i,4)
    print(f"\t{i}.0 * {n} = {m}")     # format string

print("\nExponent Table For",n,"\n")

for i in range(1,10):
    e = round(n**i,4)
    print(f"\t{n} ** {i} = {e}")

# final message
print("\n" + s)
print("\t" + s.lower())
print("\t\t" + s.title())
print("\t\t\t" + s.upper())