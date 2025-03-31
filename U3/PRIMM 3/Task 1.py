# Creating a tuple for cars

Car1 = ("Ford", "Focus", "Blue") # Creates a 3 element tuple
Car2 = ("Vauxhal", "Astra", "Red")
Car3 = ("Jaguar", "XF", "Silver")

print("-"*30)

# Print out the elements and length of each tuple
print(Car1)
print(len(Car1))

print(Car2)
print(len(Car2))

print(Car3)
print(len(Car3))

print("-"*30)

# Tuples are simply groups of data and therefore can be unpacked
(key,value1,value2) = Car1 # Defines the key and values of the tuple
print(key)      # Prints the key of the tuple
print(value1)   # Prints the 1st value of the tuple
print(value2)   # Prints the 2nd value of the tuple
