print("Welcome to the Basketball Roster Program\n")

# pg: Point Guard
# sg: Shooting Guard
# sf: Small Forward
# pf: Power Forward
# c:  Center
pg = input("Who is your point guard: ").title()
sg = input("Who is your shooting guard: ").title()
sf = input("Who is your small forward: ").title()
pf = input("Who is your power forward: ").title()
c = input("Who is your center: ").title()

print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard:\t\t",pg)
print("\t\tShooting Guard:\t\t",sg)
print("\t\tSmall Forward:\t\t",sf)
print("\t\tPower Forward:\t\t",pf)
print("\t\tCenter:\t\t\t",c)

lst = [pg, sg, sf, pf, c]   # list of all players
injured_player = sf         # Small Forward injured
lst.remove(sf)

print(f"\nOh no, {injured_player} is injured.")
print(f"Your roster only has {len(lst)} players.")
added_player = input(f"Who will take {injured_player}'s spot: ").title()
# newly added player
lst.insert(2,added_player)  # new player added to the list

print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard:\t\t",pg)
print("\t\tShooting Guard:\t\t",sg)
print("\t\tSmall Forward:\t\t",added_player)
print("\t\tPower Forward:\t\t",pf)
print("\t\tCenter:\t\t\t",c)


print(f"\nGood luck {added_player} you will do great!")
print(f"Your roster now has {len(lst)} players")

