# Challenge 29 - Item Merge
from collections import Counter

list1 = ["apple", "banana", "orange", "apple", "orange", "red"]
list2 = ["cat", "dog", "parrot", "dog", "red", "dog"]
list3 = ["red", "blue", "green", "blue", "London", "London"]
list4 = ["London", "Paris", "London", "apple", "Paris", "London"]

for l in [list2, list3, list4]:
    list1.extend(l)

print(list1)

"""
rdupe = list(dict.fromkeys(list1))

print(rdupe)
"""

# Most popular (code above = remove duplicates extension)

counter = Counter(list1)
most_common = counter.most_common(3)

print("Most common:", most_common[0][0])
print("2nd most common:", most_common[1][0])
print("3rd most common:", most_common[2][0])
