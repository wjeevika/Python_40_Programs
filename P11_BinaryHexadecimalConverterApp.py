print("Welcome to the Binary/Hexadecimal Converter App\n")

n = int(input("Compute binary and hexadecimal values up to the following decimal number: "))
print("Generating lists....complete!\n")

print("Using slices, we will now show a portion of each list.")
a = int(input("What decimal number would you like to start at: "))
b = int(input("What decimal number would you like to stop at: "))

print(f"\nDecimal values from {a} to {b}:")
for i in range(a,b+1):  print(i) 

print(f"\nBinary values from {a} to {b}:")
for i in range(a,b+1):  print(bin(i))

print(f"\nHexadecimal values from {a} to {b}:")
for i in range(a,b+1):  print(hex(i))

input(f"\nPress Enter to see all values from 1 to {n}.")
print("Decimal----Binary----Hexadecimal")
print("----------------------------------------------------------")
for i in range(1,n+1):
    print(f"{i}----{bin(i)}----{hex(i)}")

