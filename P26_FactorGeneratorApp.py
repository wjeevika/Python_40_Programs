print("Welcome to the Factor Generator App")

running = True
while(running):
    n = int(input("\nEnter a number to determine all factors of that number: "))
    print(f"\nFactors of {n} are:")
    s = []      # stores factors of number
    for i in range(1,n+1):
        if n%i == 0:
            s.append(i)
            print(i)    # printing factors

    print("\nIn summary:")
    for i in range(int(len(s)/2)):
        print(f"{s[i]} * {s[-i-1]} = {n}")

    ch = input("\nRun again (y/n): ").lower()
    if ch !='y':     # while loop will stop if True
        running = False
        print("Thank you for using the program. Have a great day.")

