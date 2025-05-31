# Challenge 45 - Tilers mate
import math

while True:
    try:
        width = float(input("Enter width of area (in metres): "))
        break
    except ValueError:
        print("Please enter a number.")

while True:
    try:
        length = float(input("Enter length of area (in metres): "))
        break
    except ValueError:
        print("Please enter a number.")

while True:
    cost_mode = input("Choose cost mode - 'per m2' or 'per tile': ").strip().lower()
    if cost_mode in ['per m2', 'per tile']:
        break
    else:
        print("Please enter 'per m2' or 'per tile'.")

area = width * length

if cost_mode == 'per m2':
    while True:
        try:
            cost_per_m2 = float(input("Enter cost per square metre: "))
            break
        except ValueError:
            print("Please enter a number.")
    total_cost = area * cost_per_m2
    print(f"\nTotal area: {area:.2f} square metres")
    print(f"Total cost: ${total_cost:.2f}")

else:
    while True:
        try:
            tile_width = float(input("Enter tile width (in metres): "))
            tile_length = float(input("Enter tile length (in metres): "))
            cost_per_tile = float(input("Enter cost per tile: "))
            break
        except ValueError:
            print("Please enter a number.")
    
    tile_area = tile_width * tile_length
    num_tiles = math.ceil(area / tile_area)
    total_cost = num_tiles * cost_per_tile
    
    print(f"\nTotal area: {area:.2f} square metres")
    print(f"Tile area: {tile_area:.2f} square metres")
    print(f"Tiles needed (rounded up): {num_tiles}")
    print(f"Total cost: ${total_cost:.2f}")
