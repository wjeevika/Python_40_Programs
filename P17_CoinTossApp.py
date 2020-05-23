import random as r      # r: alias
print("Welcome to the Coin Toss App\n")

print("I will flip a coin a set number of times.")
number = int(input("How many times would you like me to flip the coin: "))
ch = input("Would you like to see the result of each flip (y/n): ").lower()

print("\nFlipping\n")

heads = 0   # no. o heads
tails = 0   # no. of tails

# 0: HEADS
# 1: TAILS
for i in range(number):
    coin = r.randint(0,1)

    if coin == 1:
        heads+=1
        if ch.startswith('y'):
            print("HEADS")

    else:
        tails+=1
        if ch.startswith('y'):
            print("TAILS")

    if heads == tails:
        print(f"At {i+1} flips, the number of heads and tails were equal at {heads} each.")

print(f"\nResults Of Flipping A Coin {number} Times:\n")

pheads = round((heads/number)*100,2)
ptails = round((tails/number)*100,2)
print("Side\tCount\tPercentage")
print(f"Heads\t{heads}/{number}\t{pheads}%")
print(f"Tails\t{tails}/{number}\t{ptails}%")

# final answers may vary as random generates any number randomly.   
