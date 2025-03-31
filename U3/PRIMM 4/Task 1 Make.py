myFile = open("example.txt", "wt")
for i in range(5):
  information = input("Give ME a FACT about YOURSELF: ")
  myFile.write(information + "\n")

myFile.close()

myFile = open("example.txt", "rt")
contents = myFile.read()
print(contents)
myFile.close()

myFile = open("example.txt", "a")
for i in range(5):
  information = input("Give ME a FACT about THE PERSON SITTING NEXT TO YOU: ")
  myFile.write(information + "\n")

myFile.close()

myFile = open("example.txt", "rt")
contents = myFile.read()
print(contents)
myFile.close()
