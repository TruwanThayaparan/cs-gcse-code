# Challenge 13 - Count Vowels
lets_generate = input("Enter your word: ").lower()

vowel_counts = {v: 0 for v in "aeiou"}

for char in lets_generate:
    if char in vowel_counts:
        vowel_counts[char] += 1

total_vowels = sum(vowel_counts.values())

print(f"Total vowels: {total_vowels}")
for vowel, count in vowel_counts.items():
    if count > 0:
        print(f"Count of '{vowel}': {count}")
