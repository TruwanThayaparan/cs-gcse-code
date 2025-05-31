# Challenge 27 - Word Subtraction
number_dict = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,
    "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000
}

def words_to_number(text):
    text = text.lower().replace("-", " ").replace(" and ", " ")
    if text == "one million":
        return 1000000
    
    tokens = text.split()
    
    total = 0
    current = 0
    
    for word in tokens:
        if word in number_dict:
            scale = number_dict[word]
            if scale == 100:
                current *= 100
            elif scale == 1000 or scale == 1000000:
                current *= scale
                total += current
                current = 0
            else:
                current += scale
        else:
            raise ValueError(f"Unknown word: {word}")
    
    total += current
    return total

print("Welcome to Word Subtraction!")

while True:
    try:
        word1 = input("Enter first number name: ").strip()
        num1 = words_to_number(word1)
        break
    except ValueError as e:
        print(f"Error: {e}")

while True:
    try:
        word2 = input("Enter second number name: ").strip()
        num2 = words_to_number(word2)
        break
    except ValueError as e:
        print(f"Error: {e}")

if 0 <= num1 <= 127 and 0 <= num2 <= 127:
    ascii1 = chr(num1)
    ascii2 = chr(num2)
    difference = ord(ascii1) - ord(ascii2)
    print(f"ASCII character for {num1} is '{ascii1}'")
    print(f"ASCII character for {num2} is '{ascii2}'")
    print(f"Difference between ASCII values: {difference}")
else:
    print("One or both numbers are outside the ASCII range (0-127). Cannot convert to ASCII.")

# Extension
def remove_common_chars(word1, word2):
    set1 = set(word1.lower())
    set2 = set(word2.lower())
    
    common_chars = set1.intersection(set2)
    
    if not common_chars:
        return word1, word2
    
    def remove_chars(word, chars_to_remove):
        result = []
        for ch in word:
            if ch.lower() not in chars_to_remove:
                result.append(ch)
        return ''.join(result)
    
    new_word1 = remove_chars(word1, common_chars)
    new_word2 = remove_chars(word2, common_chars)
    
    return new_word1, new_word2

w1 = input("Enter a word: ")
w2 = input("Enter another word: ")
new_w1, new_w2 = remove_common_chars(w1, w2)
print(f"After removing common chars:")
print(f"Word 1: {new_w1}")
print(f"Word 2: {new_w2}")
