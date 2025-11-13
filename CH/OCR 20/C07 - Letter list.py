def find_matching_words(words, letter, mode):
    """
    Returns a list of words that match the letter according to the mode.
    mode: 'start' -> words starting with the letter
          'any'   -> words containing the letter anywhere
    """
    letter = letter.lower()
    mode = mode.lower()

    if mode == 'start':
        print(f"\nWords starting with '{letter}':")
        return [word for word in words if word.lower().startswith(letter)]
    elif mode == 'any':
        print(f"\nWords containing '{letter}' anywhere:")
        return [word for word in words if letter in word.lower()]
    else:
        print("Invalid choice. Please type 'start' or 'any'.")
        return []


def main():
    filename = input("Enter the filename containing the word list: ")

    try:
        with open(filename, 'r') as file:
            words = file.read().split()

        letter = input("Choose a letter: ").lower()
        mode = input("Type 'start' to find words starting with the letter, or 'any' to find words containing the letter anywhere: ").lower()

        matching_words = find_matching_words(words, letter, mode)

        for word in matching_words:
            print(word)

        print(f"\nTotal words found: {len(matching_words)}")

    except FileNotFoundError:
        print("The file was not found. Please check the filename and try again.")


if __name__ == "__main__":
    main()
