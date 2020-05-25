import random as r

print("Welcome to the Guess My Number App\n")

name = input("Hello! What is your name: ").title()
print(f"Well {name}, I am thinking of a number between 1 and 20.\n")

c = 0       # count variable
n = r.randint(1,20)     # generates no. between 1 to 20

while True:
    temp = int(input("Take a guess: "))
    c += 1    
    
    if temp<n:
        print("Your guess is too low.\n")

    elif temp>n:
        print("Your guess is too high.\n")

    else:   # when correct no. is identified
        print(f"\nGood job, {name}! You guessed my number in {c} guesses!")
        break

    if c == 5:      # all chances gone
        print(f"\nGame Over. The number I was thinking of was {n}")
        break

    
