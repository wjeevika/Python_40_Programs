print("Welcome to the Voter Registration App\n")

name = input("Please enter your name: ").title()
age = int(input("Please enter your age: "))

parties = ['Republican', 'Democratic', 'Independent', 'Libertarian', 'Green']
# list of all the parties

if age<18:
    print("\nYou are not old enough to register to vote.")

else:   # for age >= 18
    print(f"\nCongratulations {name}! You are old enough to register to vote.\n")
    print("Here is a list of political parties to join.")
    for i in parties:   # displays all parties
        print(f"\t- {i}")

    pt = input("\nWhat party would you like to join: ").title()
    if pt in parties:   # message to display when party is chosen
        print(f"\nCongratulations {name}! You have joines the {pt} party!")
        if pt == "Republican" or pt == "Democratic":
            print("That is a major party!")

        elif pt == "Independent":
            print("You are an independent person!")

        else:
            print("That is not a major party.")

    else:   # if chosen party is not in parties list
        print("That is not a given party.")

