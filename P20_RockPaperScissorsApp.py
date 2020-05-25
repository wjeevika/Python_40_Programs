import random as r

print("Welcome to a game of Rock, Paper, Scissors\n")
try:
    n = int(input("How many rounds would you like to play: "))

    play = 0    # player scores
    comp = 0    # computer scores

    moves = ['rock', 'paper', 'scissors']
    # 0: rock
    # 1: paper
    # 2: scissors

    for i in range(n): # to check no. of rounds played 

        print(f"\nRound {i+1}")
        print(f"Player: {play}\tComputer: {comp}")  # displays scores of player and computer
        p_choice = input("Time to pick...rock, paper, scissors: ").lower().strip()
        
        
        if p_choice in moves:
            ch = r.randint(0,2)
            c_choice = moves[ch]
            print(f"\tComputer: {c_choice}")
            print(f"\tPlayer: {p_choice}")

            # computer chooses rock
            if p_choice == 'rock' and c_choice == 'rock':
                winner = 'tie'
            elif p_choice == 'paper' and c_choice == 'rock':
                winner = p_choice
                phase = 'Paper covers rock!'
            elif p_choice == 'scissors' and c_choice == 'rock':
                winner = c_choice
                phase = 'Rock smashes scissors!'
            # computer chooses paper
            elif p_choice == 'rock' and c_choice == 'paper':
                winner = c_choice
                phase = 'Paper covers rock'
            elif p_choice == 'paper' and c_choice == 'paper':
                winner = 'tie'
            elif p_choice == 'scissors' and c_choice == 'paper':
                winner =  p_choice
                phase = 'Scissors cut paper!'
            # computer chooses scissors
            elif p_choice =='rock' and c_choice == 'scissors':
                winner = p_choice
                phase = 'Rock smashes scissors!'
            elif p_choice == 'paper' and c_choice == 'scissors':
                winner = c_choice
                phase = 'Scissors cut paper!'
            elif p_choice == 'scissors' and c_choice == 'scissors':
                winner = 'tie'

            
            if winner == p_choice:
                play +=1
                print("\t"+phase)
                print(f"\tYou win round {i+1}")
            elif winner == c_choice:
                comp +=1
                print("\t"+phase)
                print(f"\tComputer gets the point")
            else:
                print("\tIt is a tie, how boring!")
                print("\tsThis round was a tie.")

        else:
            comp +=1
            print("That is not a valid game option!")
            print("Computer gets the point!")


    print("\nFinal Game Results")
    print(f"\tRounds Played: {n}")
    print(f"\tPlayer Score: {play}")
    print(f"\tComputer Score: {comp}")

    if play>comp:   # computes winner
        print("\tWinner: PLAYER!!!")
    elif play<comp:
        print("\tWinner: Computer :-(")
    else:
        print("\tThe game was a tie.")

# if user doesn't enter an integer for no. of rounds to be played
except:
    print("Retry and enter an a positive integer.")



