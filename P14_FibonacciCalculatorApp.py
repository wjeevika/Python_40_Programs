print("Welcome to the Fibonacci Calculator App\n")

n = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

# gives the upper limit
print(f"\n The first {n} numbers of the Fibonacci sequence are:")

fib = [1, 1]    # list stores all fibonacci numbers till upper limit
for i in range(n-2):
    nf = fib[i] + fib[i+1]
    fib.append(nf)

for i in range(n):  # printing fibonacci numbers
    print(fib[i])

print("\nThe corresponding Golden Ratio values are:")
for i in range(n-1):
    print(fib[i+1]/fib[i])      # printing golden ratio

print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...")

