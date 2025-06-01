# Challenge 7 - Letter list

letter = input("Choose a letter: ").lower()
choice = input("Type 'start' to find words starting with the letter, or 'any' to find words containing the letter anywhere: ")

if choice == 'start':
    matching_words = [word for word in words if word.lower().startswith(letter)]
    print(f"Words starting with '{letter}':")
elif choice == 'any':
    matching_words = [word for word in words if letter in word.lower()]
    print(f"Words containing '{letter}' anywhere:")
else:
    print("Invalid choice. Please type 'start' or 'any'.")
    matching_words = []

for word in matching_words:
    print(word)

print(f"Total words found: {len(matching_words)}")


filename = input("Enter the filename containing the word list: ")

try:
    with open(filename, 'r') as file:
        words = file.read().split()
        
    letter = input("Choose a letter: ").lower()
    choice = input("Type 'start' to find words starting with the letter, or 'any' to find words containing the letter anywhere: ").lower()
    
    if choice == 'start':
        matching_words = [word for word in words if word.lower().startswith(letter)]
        print(f"Words starting with '{letter}':")
    elif choice == 'any':
        matching_words = [word for word in words if letter in word.lower()]
        print(f"Words containing '{letter}' anywhere:")
    else:
        print("Invalid choice. Please type 'start' or 'any'.")
        matching_words = []
    
    for word in matching_words:
        print(word)
    
    print(f"Total words found: {len(matching_words)}")
    
except FileNotFoundError:
    print("The file was not found. Please check the filename and try again.")
