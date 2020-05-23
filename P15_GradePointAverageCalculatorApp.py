print("Welcome to the Average Calculator App\n")

name = input("What is your name: ").title()
n = int(input("How many grades would you like to enter: "))

s = []
for _ in range(n):
    i = int(input("Enter grade: "))
    s.append(i)

s = sorted(s, reverse= True)
temp = s[:]     # creates a new list temp with same values as s
print("Grades Highest to Lowest:")
for i in range(n):
    print(f"\t{s[i]}")

print(f"\n{name}\'s Grade Summary:")
print(f"\tTotal Number of Grades: {n}")
print("\tHighest Grade:",max(s))
print("\tLowest Grade:",min(s))
a1 = round(sum(s)/n,2)
print("\tAverage: ", a1)

avg = float(input("\nWhat is your desired average: "))

print("\nGood luck Mike!")
extra = float((n+1)*avg - sum(s))   # calculates the marks  required in next test

print(f"You will need to get a {extra} on your next assignment to earn a {avg} average.")

print("\nLets see what your average could have been if you did better/worse on an assignment.")
change = int(input("What grade would you like to change: "))
s.remove(change)    # desired grade removed
changeTo = int(input(f"What grade would you like to change {change} to: "))
s.append(changeTo)  # desired grade added

s = sorted(s, reverse= True)
print("\nNew Grades Highest to Lowest:")
for i in range(n):
    print(s[i])
print(f"\n{name}\'s New Grade Summary:")
print(f"\tTotal Number of Grades: {n}")
print("\tHighest Grade:",max(s))
print("\tLowest Grade:",min(s))
a2 = round(sum(s)/n,2)  # new average
print("\tAverage: ", a2)

print(f"\nYour new average would be a {a2} compared to your real average of {a1}!")
diff = round(a2-a1,1)
print(f"That is a change of {diff} points!")

print("\nToo bad your original grades are still the same!")
print(temp)
print("You should go ask for extra credit!")

