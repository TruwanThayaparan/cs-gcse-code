# Challenge 36 - Triangulate

# triangle inequality theorem
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

def is_right_angle(a, b, c):
    sides = sorted([a, b, c])
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-10

def check():
    try:
        a = float(input("Enter side 1: "))
        b = float(input("Enter side 2: "))
        c = float(input("Enter side 3: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if not is_triangle(a, b, c):
        print("These sides do NOT form a triangle.")
        return

    t_type = triangle_type(a, b, c)
    right = is_right_angle(a, b, c)

    if right:
        print(f"The triangle is Right-Angled {t_type}.")
    else:
        print(f"The triangle is {t_type}.")

check()
