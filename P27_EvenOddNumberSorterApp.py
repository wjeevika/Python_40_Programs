print("Welcome to the Prime Number App\n")

running = True
while running:
    n = input("Enter in a string of numbers separated by a comma(,): ")
    n = n.replace(' ','')   # removing spaces before and after ,
    s = n.split(",")

    e = []  # to append even elements
    o = []  # to append odd elements

    print("---- Result Summary ----")
    for i in range(len(s)):
        if int(s[i])%2 == 0:
            e.append(s[i])      # even list
            print(f"\t{s[i]} is even!")
        else:
            o.append(s[i])      # odd list
            print(f"\t{s[i]} is odd!")

    print(f"\nThe following {len(e)} are even:")
    for i in range(len(e)):
        print("\t",e[i])

    print(f"\nThe following {len(o)} are odd:")
    for i in range(len(o)):
        print("\t",o[i])

    ch = input("\nWould you like to run the program again (y/n): ").lower()
    if ch != 'y':
        running = False
        print("Thank you for using the program. Goodbye.")

    


