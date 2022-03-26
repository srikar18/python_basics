# https://youtu.be/bD05uGo_sVI

def square_num(numbers):
    res = []
    for num in numbers:
        res.append(num ** 2)
    return res


s1 = square_num([1, 2, 3, 4, 5])
print("Using normal function ", s1)

# using generator


def square_num_gen(numbers):
    for num in numbers:
        yield(num**2)


s1 = square_num_gen([1, 2, 3, 4, 5])

print("Using generator")

for num in s1:
    print(num)

# using list comprehension and generator
s1 = (x*x for x in [1, 2, 3, 4, 5])

print("Using generator and list comprehension")

for num in s1:
    print(num)

# generator does not hold values in memory
# when you print a genrator you get an address
# to get values, call next() on generator object
# to convert generator to a list use list() function
