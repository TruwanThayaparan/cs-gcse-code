# Challenge 13 - Caesar Cipher

print("Welcome to the Caesar Cipher Encryptor/Decryptor!")

def menu():
  while True:
    mode = input("\nDo you want to decrypt or encrypt a message? ").strip().lower()

    if mode in ("exit", "quit", "stop"):
        print("Script ended.")
        return
      
    if mode not in ("decrypt", "encrypt"):
        print(f"{mode} is not a valid mode. Please try again.")
        continue
    
    break
    
  message = input(f"Enter the message you want to {mode}: ")

  while True:
    try:
      key = int(input("Enter the amount of shifts for your message: ").strip())
      if 1 <= key <= 25:
        break
      print("You must enter an integer between 1 and 25.")
    except ValueError:
      print("You must enter an integer.")

  final = run_cipher(message, key, mode)
  print(f"\nThe {mode}ed message is: {final}.")

def run_cipher(message, key, mode):
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

    final = ''.join(result)
    return final

menu()
