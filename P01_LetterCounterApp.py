print("Welcome to the Letter Counter App\n")

s = input("What is your name: ")
print(f"\nHello {s.capitalize()}!")

print("I will count the number of times that a specific letter occurs in a message.")
m = input("\nPlease enter a message: ")
n = input("Which letter would you like to count the occurrences of: ")

c=0     
for i in m.lower():
    if n.lower()==i:       # to make sure both upper and lower case are searched
        c+=1

print(f"{s.capitalize()}, your message has {c} {n}\'s in it.")      # final output

