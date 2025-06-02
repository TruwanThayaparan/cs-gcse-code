# Challenge 55 - Secret Ciphers

def vigenere(text, key, mode):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            if is_upper:
              base = ord('A')
            else:
              base = ord('a')

            t = ord(char.lower()) - ord('a')
            k = ord(key[key_index % len(key)]) - ord('a')

            if mode == 'encrypt':
              shifted = (t + k) % 26 
            else:
              shifted = (t - k + 26) % 26
            new_char = chr(shifted + base)
            result += new_char

            key_index += 1
        else:
            result += char

    return result

def caesar(message, key, mode):
    result = []

    for char in message:
        if char.isalpha():
            if char.isupper():
                offset = 65 
            else:
                offset = 97

            if mode == "decrypt":
              shift = -key
            else: 
              shift = key

            new_char = chr((ord(char) - offset + shift) % 26 + offset)
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

def vernam(text, key):
    result = ""

    for t_char, k_char in zip(text, key):
        xor_result = ord(t_char) ^ ord(k_char)
        result += chr(xor_result)

    return result

print("Welcome to the Encryptor/Decryptor!")


def menu():
    while True:
        while True:
            cipher = input("Choose a cipher ('vigenere', 'caesar' or 'vernam'): ").strip().lower()
            if cipher not in ("vigenere", "caesar", "vernam"):
                print(f"{cipher} is not a valid cipher. Please try again.")
                continue
            break

        if cipher in ("vigenere", "caesar"):
            while True:
                mode = input("\nDo you want to decrypt or encrypt a message? ").strip().lower()
                if mode not in ("decrypt", "encrypt"):
                    print(f"{mode} is not a valid mode. Please try again.")
                    continue
                break

            message = input(f"Enter the message you want to {mode}: ")

            if cipher == "vigenere":
                key = input("Enter the keyword for the Vigenère cipher: ").replace(" ", "")
                final = vigenere(message, key, mode)
            elif cipher == "caesar":
                while True:
                    try:
                        key = int(input("Enter the numeric key (0–25) for the Caesar cipher: "))
                        if 0 <= key <= 25:
                            break
                        else:
                            print("Please enter a number between 0 and 25.")
                    except ValueError:
                        print("That’s not a valid number.")
                final = caesar(message, key, mode)

        elif cipher == "vernam":
            message = input("Enter the message: ")
            while True:
                key = input("Enter a key the same length as your message: ")
                if len(key) != len(message):
                    print("Error: The key must be the same length as the message for the Vernam cipher.")
                    continue
                break
            final = vernam(message, key)
            mode = "processed"

        print(f"\nThe {mode.title()}ed message is: {final}\n")

        keep_going = input("Do you want to decrypt/encrypt another message? (yes/no): ")
        if keep_going.strip().lower() in ("no", "n"):
            print("Script ended.")
            break
menu()
