# https://youtu.be/DZwmZ8Usvnk
# Comparisions 
    #  equals to ==
    #  not equals to !=
    #  greater than >
    #  less than <
    #  greater than or equals to >=
    #  less than or equals to <=
    #  object identity "is"
    #  and => evalues to true if all conditions are met
    #  or => evaluates to true if any one condition is met
    #  not => switches the boolean value i.e, True to False and vice-versa

#  short circuiting https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

# False values
    # False
    # None
    # Zero of any numeric type
    # any empty sequence i.e, (),[],''
    # any empty mapping i.e, {}

# if 
if True:
    print("inside if condition")


# if else 
language = 'python'

if language == 'python':
    print("Language is python")
else:
    print("Language is not python")

# elif 
language = 'java'

if language == 'python':
    print("Language is python")
elif language == 'java':
    print("Language is java")
else:
    print("Language not found")

# AND
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print("Access permitted")
else:
    print("Access denied")

# OR
a = 5
if a < 0 or a > 3:
    print("a falls in range")
else:
    print("a falls outside of range")

# NOT

if not logged_in:
    print("Please login")
else:
    print("Welcome :)")

# is operator checks for memory reference i.e, checks if their ids are equal
a = [1,2,3,4]
b = [1,2,3,4]
c = b

print(a == b) # True as values are compared
print(a is b) # False as b is a different list and not a reference to a
print(c is b) # True as c is reference to b