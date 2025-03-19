word = input("Input a word: ")
word2 = input("Input another word: ")
checked = []
correct = 0
if len(word) == len(word2):
  for i in range(len(word)):
    for j in range(len(word)):
        print(i, j, word[i], word2[j])
        if word[i] == word2[j]:
            if j not in checked:
                correct += 1
                checked.append(j)
                print(correct)
                break
            
    
  if correct == len(word):
        print("Anagramed.")
  else:
        print("Not anagramed.")
else:
    print("Not anagramed.")

'''
 if sorted(word) == sorted(word2):
        print("Anagramed.")
    else:
        print("Not anagramed.")
'''
