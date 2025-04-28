# Challenge 61 - Your name is...
name = input("What is your name? ")
age = input("What is your age? ")
form = input("What form are you in? ")
details = "Your name is " + name + ", you are " + age + ", and you are in form " + form + "."
print(details)

myFile = open("details.txt", "wt")
myFile.write(details + "\n")
myFile.close()
