print("\t\tSummary Table")

# hard coding the values
num_strings = ['15', '100', '55', '42']
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# display message
print("\nThe variable num_strings is a " + str(type(num_strings)) + ".")
print("It contains the elements:",num_strings)
print(f"The element {num_strings[0]} is a " + str(type(num_strings[0])) + ".")

print("\nThe variable num_ints is a " + str(type(num_ints)) + ".")
print("It contains the elements:",num_ints)
print(f"The element {num_ints[0]} is a " + str(type(num_ints[0])) + ".")

print("\nThe variable num_floats is a " + str(type(num_floats)) + ".")
print("It contains the elements:",num_floats)
print(f"The element {num_floats[0]} is a " + str(type(num_floats[0])) + ".")

print("\nThe variable num_lists is a " + str(type(num_lists)) + ".")
print("It contains the elements:",num_lists)
print(f"The element {num_lists[0]} is a " + str(type(num_lists[0])) + ".")

print("\nNow sorting num_strings and num_ints...")
print("Sorted num_strings:",sorted(num_strings))    
print("Sorted num_ints:",sorted(num_ints))          

print("\nStrings are sorted aplhabetically while integers are sorted numerically!")