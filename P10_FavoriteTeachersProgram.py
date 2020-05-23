print("Welcome to the Favorite Teachers Program\n")

# order for favorite teachers
order = ['first', 'second', 'third', 'fourth']
s = []

for i in order:
    a = input(f"Who is your {i} favorite teacher: ").title()
    s.append(a)

print("\nYour favorite teachers ranked are:",s) # ranked as per entered by user
print("Your favorite teachers alphabetically are:",sorted(s))
print("Your favorite teachers in reverse alphabetical order are:",sorted(s, reverse= True))

print(f"\nYour top two teachers are: {s[0]} and {s[1]}.")
print(f"Your next two favorite teachers are: {s[2]} and {s[3]}.")
print(f"Your last favorite teacher is: {s[-1]}.")   # always the last teacher
print(f"You have a total of {len(s)} favorite teachers.\n")

print(f"Oops, {s[0]} is no longer your first favorite teacher.", end= " ")  # not removed now
nw = input("Who is your new FAVORITE teacher: ").title()
s.insert(0,nw)

print("\nYour favorite teachers ranked are:",s)
print("Your favorite teachers alphabetically are:",sorted(s))
print("Your favorite teachers in reverse alphabetical order are:",sorted(s, reverse= True))

print(f"\nYour top two teachers are: {s[0]} and {s[1]}.")
print(f"Your next two favorite teachers are: {s[2]} and {s[3]}.")
print(f"Your last favorite teacher is: {s[-1]}.")
print(f"You have a total of {len(s)} favorite teachers.\n")

print("You've decided you no longer like a teacher.", end= " ")
nw = input("Which teacher would you like to remove from you list: ").title()
s.remove(nw)    # teacher removed from the list

print("\nYour favorite teachers ranked are:",s)
print("Your favorite teachers alphabetically are:",sorted(s))
print("Your favorite teachers in reverse alphabetical order are:",sorted(s, reverse= True))

print(f"\nYour top two teachers are: {s[0]} and {s[1]}.")
print(f"Your next two favorite teachers are: {s[2]} and {s[3]}.")
print(f"Your last favorite teacher is: {s[-1]}.")
print(f"You have a total of {len(s)} favorite teachers.\n")


