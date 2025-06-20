# Creating the most unoptimised code... ever.

j = []

for i in range(1, 101):
    j.append(i)
    print(j[i - 1])
    
print("\nPrinted all numbers between 1 and 100\n")
    
items = [1, 2, 3, 4]
x = -1
while True:
    x += 1
    try:
        c = items[x]
    except:
        break
    
print(f"\nCounted {x} items.\n")
