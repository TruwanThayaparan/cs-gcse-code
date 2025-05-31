# Challenge 32 - Code it up
def encode_string(s, shift):
    result = ""
    for char in s:
        result += chr(ord(char) + shift)
    return result

def decode_string(s, shift):
    result = ""
    for char in s:
        result += chr(ord(char) - shift)
    return result

def main():
  while True:
    print("1. Encode a string")
    print("2. Decode a string")
    print("3. Exit")

    choice = input("Choose an option (1-3): ").strip().lower()

    if choice in ["1", "encode"]:
        user_input = input("Enter a string to encode: ")
        while True:
            try:
                shift = int(input("Enter shift amount: "))
                break
            except ValueError:
                print("Shift must be a number.")
        encoded = encode_string(user_input, shift)
        print("Encoded string:", encoded)

    elif choice in ["2", "decode"]:
        user_input = input("Enter a string to decode: ")
        while True:
            try:
                shift = int(input("Enter shift amount used for encoding: "))
                break
            except ValueError:
                print("Shift must be a number.")
        decoded = decode_string(user_input, shift)
        print("Decoded string:", decoded)

    elif choice in ["3", "exit", "quit", "stop"]:
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

main()
