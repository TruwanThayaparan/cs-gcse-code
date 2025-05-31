# Challenge 65 - Spam filter
import random

dishes = [
  "Eggs Benedict", 
  "Pancakes with syrup", 
  "Grilled cheese sandwich", 
  "Caesar salad", 
  "Tomato soup", 
  "Roast chicken", 
  "Fish and chips", 
]

spam_dishes = []

for dish in dishes:
    words = dish.split(' ')

    new_words = []
    for i, word in enumerate(words):
        new_words.append(word)
        if i < len(words) - 1 and random.choice([True, False]):
            new_words.append("Spam")
    
    if random.choice([True, False]):
        new_words.insert(0, "Spam")
    if random.choice([True, False]):
        new_words.append("Spam")
    
    spam_dishes.append(" ".join(new_words))

for sd in spam_dishes:
    print(sd)
