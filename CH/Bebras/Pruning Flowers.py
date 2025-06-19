sentence = input()
words = sentence.split()

seen = set()
result = []

for word in words:
    if word not in seen:
        seen.add(word)
        result.append(word)

print(" ".join(result))
