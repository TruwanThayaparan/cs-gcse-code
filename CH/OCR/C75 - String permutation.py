# Challenge 75 - String permutation
from collections import Counter

def longest_common_permuted_subsequence(x: str, y: str) -> str:
    count_x = Counter(x)
    count_y = Counter(y)
    
    common_letters = count_x & count_y 
    
    result = []
    for letter, freq in common_letters.items():
        result.append(letter * freq)

    return ''.join(result)
    #return ''.join(sorted(result))

x = input("Enter a string: ").strip()
y = input("Enter another string: ").strip()
print(f"Longest common permuted subsequence: {longest_common_permuted_subsequence(x, y)}")
