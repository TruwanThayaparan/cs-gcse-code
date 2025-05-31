# Challenge 33 - Mor-se Coding

# morse code dictionary
morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '|'
}

# reversed dictionary
reverse_morse_dict = {value: key for key, value in morse_code_dict.items()}

# Encoding
text_to_encode = input("Enter a string to encode: ").upper().strip()
encoded = ""
for char in text_to_encode:
    code = morse_code_dict.get(char, '?')
    encoded += code + " "

print(f"Encoded Morse Code: {encoded.strip()}")

# Decoding
morse_to_decode = input("\nEnter Morse code to decode (use space between letters, '|' for space): ").strip()
decoded = ""
for code in morse_to_decode.split(" "):
    decoded += reverse_morse_dict.get(code, '?')

print(f"Decoded Text: {decoded}")
