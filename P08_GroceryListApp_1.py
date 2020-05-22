import datetime

time = datetime.datetime.now()
month = time.month
day = time.day
hour = time.hour
minute = time.minute
print("Welcome to the Grocery List App.")
print(f"Current Date and Time: {month}/{day} {hour}:{minute}")

s = ['Meat', 'Cheese']

print(f"You currently have {s[0]} and {s[1]} in your list.\n")

a = input("Type of food to add to the grocery list: ")
s.append(a.title())
a = input("Type of food to add to the grocery list: ")
s.append(a.title())
a = input("Type of food to add to the grocery list: ")
s.append(a.title())

print("\nHere is your grocery list:")
print(s)
print("Here is your grocery list sorted:")
s = sorted(s)
print(s)

print("\nSimulating grocery shopping...\n")


print(f"Current grocery list: {len(s)} items")
print(s)
i = input("What food did you just buy: ").title()
s.remove(i)
print(f"Removing {i} from list...\n")

print(f"Current grocery list: {len(s)} items")
print(s)
i = input("What food did you just buy: ").title()
s.remove(i)
print(f"Removing {i} from list...\n")

print(f"Current grocery list: {len(s)} items")
print(s)
i = input("What food did you just buy: ").title()
s.remove(i)
print(f"Removing {i} from list...\n")

print(f"Current grocery list: {len(s)} items")
print(s)

print(f"\nSorry, the store is out of {s[1]}.")
a = input("What food would you like instead: ").title()
s.pop()
s.insert(0,a)
print("\nHere is what remains on your grocery list:")
print(s)

