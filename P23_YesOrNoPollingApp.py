print("Welcome to the Yes or No Issue Polling App\n")

result = {} # dictionary to store results of all voters

v = 0
issue = input("What is the yes or no issue you will be voting on today: ")
n = int(input("What is the number of voters you will allow on the issue: "))
password = input("Enter a password for polling results: ")

for i in range(n):  # loop to take votes
    name = input("\nEnter your full name: ").title()
    if name in result:  # if one has already voted
        print("Sorry, it seems that someone with that name has already voted.")
        
    else:   
        print(f"Here is our issue: {issue}")
        ch = input("What do you think...yes or no: ").lower()
        if ch == 'n':
            ch = 'no'
        elif ch == 'y' or ch == 'ye':
            ch = 'yes'
        print(f"Thank you {name}! Your vote of {ch} has been recorded.")
        result[name] = ch   # updating dictionary
        v +=1
    
print(f"\nThe following {v} people voted:")
y = 0   # counts yes
no = 0  # counts no
for i in result.keys():
    print(i)    # printing names of voters
    if result[i] == 'yes':  # counting yes and no
        y += 1
    else:
        no += 1

print(f"\nOn the following issue: {issue}")     # to display who wins
if y>no:
    print(f"Yes wins! {y} votes to {n}.")
elif no>y:
    print(f"Yes wins! {no} votes to {y}.")
else:
    print(f"It was a tie! {y} votes to {y}")
    
admin = input("To see the voting results enter the admin password: ")
if admin == password:
    for i in result.keys():
        print(f"Voter: {i}\tVote: {result[i]}")
else:
    print("Sorry, that is not the correct password. Goodbye...")

print("\nThank you for using the Yes or No Issue Polling App.")

