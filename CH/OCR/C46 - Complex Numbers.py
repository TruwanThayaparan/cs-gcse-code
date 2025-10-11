# Challenge 46 - Complex Numbers

# adding
def add_complex(z1, z2):
    return z1 + z2

# multiplying
def multiply_complex(z1, z2):
    return z1 * z2

# negating
def negate_complex(z):
    return -z

# inversing
def inverse_complex(z):
    if z == 0:
        return "Inverse does not exist for zero."
    else:
        return 1 / z

# main code
def test_complex_operations():
    z1 = 3 + 4j
    z2 = 1 + 2j
    
    # add
    addition_result = add_complex(z1, z2)
    print(f"Addition of {z1} and {z2} = {addition_result}")
    
    # multiply
    multiplication_result = multiply_complex(z1, z2)
    print(f"Multiplication of {z1} and {z2} = {multiplication_result}")
    
    # negation
    negation_result = negate_complex(z1)
    print(f"Negation of {z1} = {negation_result}")
    
    # inverse
    inverse_result = inverse_complex(z1)
    print(f"Inverse of {z1} = {inverse_result}")
    
    # subtraction (derived from negation + addition)
    subtraction_result = add_complex(z1, negate_complex(z2))
    print(f"Subtraction of {z1} and {z2} = {subtraction_result}")
    
    # division (derived from multiplication by inverse)
    division_result = multiply_complex(z1, inverse_complex(z2))
    print(f"Division of {z1} by {z2} = {division_result}")

test_complex_operations()
