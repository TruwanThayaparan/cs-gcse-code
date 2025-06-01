# Challenge 11 - Count Words in a String

text = input("Enter a string: ")
splits = text.split(' ')
    
print(f"There are {len(splits)} words in the string.")


filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        text = file.read()
        splits = text.split()
        print(f"There are {len(splits)} words in the file.")
except FileNotFoundError:
    print("The file was not found. Please check the filename and try again.")
