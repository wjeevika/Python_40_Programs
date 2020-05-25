import random as r

thesaurus = {"hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
"cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
"happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
"sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']}   # dictionary of all words

print("Welcome to the Thesaurus App!\n")

print("Choose a word from the thesaurus and I will give you a synonym.")

print("\nHere are the words in the thesaurus:")
for i in thesaurus.keys():  # prints keys in the dictionary
    print("\t-"+i)

s = input("\nWhat word would you like a synonym for: ").lower()
if s in thesaurus.keys():
    i = r.randint(0,4)  # generates any number to access synonyms from the dictionary 
    print(f"A synonym for {s} is {thesaurus[s][i]}\n")
else:
    print("I'm sorry, that word is not currently in the thesaurus.\n")


ch = input("Would you like to see the whole therasus (yes/no): ").lower()
if ch == 'no':
    print("\nI hope you enjoyed the program. Thank you!")

else: 
    for i in thesaurus.keys():                  # whole thesaurus
        print(f"{i.title()} synonyms are:")
        for j in thesaurus[i]:
            print(f"\t-{j}")

