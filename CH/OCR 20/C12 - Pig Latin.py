# Challenge 12 - Pig Latin
word = input("Enter a word to be converted to Pig Latin: ")
if word[0].lower() not in ["a", "e", "i", "o", "u"]:
    word_keep = word[0]
    word = word[1:]
    word += "-" + word_keep + "ay"
else:
    word += "-yay"
print(word)
