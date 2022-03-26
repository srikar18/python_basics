# https://youtu.be/khKv-8q7YmY
# Arithmetic Operators:
    # Addition:       3 + 2 = 5
    # Subtraction:    3 - 2 = 1
    # Multiplication: 3 * 2 = 6
    # Division:       3 / 2 = 1.5 (for python2, returns 1)
    # Floor Division: 3 // 2 = 1
    # Exponent:       3 ** 2 = 9
    # Modulus:        3 % 2 = 1


# Comparisons:
    # Equal:            3 == 2 False
    # Not Equal:        3 != 2 True
    # Greater Than:     3 > 2 True
    # Less Than:        3 < 2 False
    # Greater or Equal: 3 >= 2 True
    # Less or Equal:    3 <= 2 False

num = 3
print(type(num))

dec = 3.79

print("{0} rounded off to {1}".format(dec,round(dec)))

# CAST INTO NUM OR FLOAT

num_1 = '100'
num_2 = '200'

print(f"{num_1} + {num_2} = {num_1 + num_2}")

# with type conversion
print(f"{num_1} + {num_2} = {int(num_1) + int(num_2)}")
