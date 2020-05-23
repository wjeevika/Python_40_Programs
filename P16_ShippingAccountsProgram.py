print("Welcome to the Shipping Accounts Program\n")

users = ['eramom', 'footea', 'davisv', 'papinukt', 'allenj']
# list of all our users 

name  = input("Hello, what is your username: ").lower()     # accepts all cases

if name in users:       # main condition
    print(f"\nHello {name}. Welcome back to your account.")
    print("Current shipping prices are as follows:\n")

    print("Shipping orders 0 to 100:\t\t$5.10 each")
    print("Shipping orders 100 to 500:\t\t$5.00 each")
    print("Shipping orders 500 to 1000:\t\t$4.95 each")
    print("Shipping orders over 1000:\t\t$4.80 each")

    n = int(input("How many items would you like to ship: "))
    if 0<n<100:
        rate = 5.10
    elif n<500:
        rate = 5.00
    elif n<1000:
        rate = 4.95
    else:
        rate = 4.80

    amount = round(n*rate,2)
    print(f"To ship {n} items it will cost you ${amount} at ${rate} per item.\n")

    ch = input("Would you like to place this order (y/n): ").lower()
    if ch == 'y':
        print(f"Okay. Shipping your {n} items.")
    else:
        print("Okay, no order is being placed at this time.")

else:       # end of main condition
    print("Sorry, you do not have an account with us. Goodbye.")



    
