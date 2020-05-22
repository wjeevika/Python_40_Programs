print("Welcome to the Basketball Roster Program\n")

roles = ['point guard', 'shooting guard', 'small forward', 'power forward', 'center']
lst = []   # list of all players

for i in range(len(roles)):
    r = input(f"Who is your {roles[i]}: ").title()
    lst.append(r)


print("\n\tYour starting 5 for the upcoming basketball season")
for i in range(len(roles)):
    r = roles[i].title()
    if i == len(roles) - 1:     # to properly align the list
        print(f"\t\t{r}:\t\t\t",lst[i]) 
        break
    print(f"\t\t{r}:\t\t",lst[i])
    

injured_player = lst[2]        # Small Forward injured
lst.pop(2)

print(f"\nOh no, {injured_player} is injured.")
print(f"Your roster only has {len(lst)} players.")
added_player = input(f"Who will take {injured_player}'s spot: ").title()    # newly added player
lst.insert(2,added_player)  # new player added to the list

print("\n\tYour starting 5 for the upcoming basketball season")

for i in range(len(lst)):
    r = roles[i].title()
    if i == len(lst) - 1:       # to align list in tabular format
        print(f"\t\t{r}:\t\t\t",lst[i])
        break
    print(f"\t\t{r}:\t\t",lst[i])
    

print(f"\nGood luck {added_player} you will do great!")
print(f"Your roster now has {len(lst)} players")

