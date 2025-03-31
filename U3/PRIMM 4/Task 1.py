# Write a file
myFile = open("example.txt", "wt")
myFile.write("I have written to a file. \n")
myFile.write("It now has 3 lines. \n")
myFile.write("The third being this one. \n")
myFile.close()

# Append to a file
myFile = open("example.txt", "a")
myFile.write("PS: Here is another line I forgot to add! \n")
myFile.close()

# Reading a file
myFile = open("example.txt", "rt")
contents = myFile.read()
print(contents)
myFile.close()
