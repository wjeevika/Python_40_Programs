from collections import Counter

print("Welcome to the Frequency Analysis App\n")

# list of all elements to be removed from the string entered
non =  ['1','2','3','4','5','6','7','8','9','0',' ',
'.','?','!',',','"',"'",':',';','(',')','%','$','&','#','\n','\t']

for m in range(1,3):    # to perform its function only 2 times

    ph = input("Enter a word or phrase to count the occurrence of each letter: ").lower().strip()

    for j in non:   # reolacing all non elements in string with no space
        ph = ph.replace(j, '')

    letter = Counter(ph)    # creates a dictionary of elements with their occurences
    length = len(ph)
    print(f"\nHere is the frequency analysis from key phrase {m}:\n")
    print(f"\tLetter\t\tOccurence\tPercentage")
    for key, value in sorted(letter.items()):   # to display alphabetically
        percentage = value*100/length
        percentage = round(percentage,2)
        print(f"\t{key}\t\t{value}\t\t{percentage}%")   # displays result 

    ordPh = letter.most_common()    # to get elements with highest frequency in an order
    s = []
    for pair in ordPh:     # ordPh is a list with tuple pairs in it
        s.append(pair[0])  
    print("\nLetters ordered from highest occurrence to lowest:")
    for i in s:
        print(i, end = '')
    print("\n")
       
