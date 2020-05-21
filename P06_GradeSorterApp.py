print("Welcome to the Grade Sorter App\n")

a = int(input("What is your first grade (0-100): "))
b = int(input("What is your second grade (0-100): "))
c = int(input("What is your third grade (0-100): "))
d = int(input("What is your fourth grade (0-100): "))

ls = [a,b,c,d]

print("\nYour grades are:",ls)

ls = sorted(ls, reverse=True)   # sorted list
print("\nYour grades from highest to lowest are: ",ls)

print("\nThe lowest two grades will now be dropped")    
print("Removed grade:",ls.pop())    # lowest grade
print("Removed grade:",ls.pop())    # second lowest grade

print("\nYour remaining grades are:",ls)
print("Nice work! Your highest grade is a",ls[0])   # highest at 0 index
