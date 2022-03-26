# https://youtu.be/x3v9zMX1s4s
# Duck typing and easier to ask forgiveness than permissions (EAFP)
# pythonic” describes a coding style that leverages Python's unique features to write code that is readable and beautiful

# DUCK TYPING
# focus on what the object can do, instead of what it is
# we dont care what object we are dealing with, we only care if it does what we ask it to do
# https://stackoverflow.com/questions/4205130/what-is-duck-typing


class Duck:
    def quack(self):
        print('Quack, quack!')

    def fly(self):
        print('Flap, flap!')


class Person:
    def quack(self):
        print("I'm quacking like a duck")

    def fly(self):
        print("I'm flapping my arms")


def quack_and_fly(thing):
    # not duck typing (non pythonic)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('Must be a Duck!')

    print()


def duck_typing(thing):
    thing.quack()
    thing.fly()

    print()


# not EAFP
# non-pythonic 
# this is referred to as look before you leap (LBYl)
def quack_and_fly_1(thing):
    if hasattr(thing, 'quack') and callable(thing.quack):
        thing.quack()
    
    if hasattr(thing, 'fly') and callable(thing.fly):
        thing.fly()
    
    print()

def eafp_method(thing):
    try:
        thing.quack()
        thing.fly()
        print()
    except AttributeError as e:
        print(e)

d = Duck()
quack_and_fly(d)
duck_typing(d)
quack_and_fly_1(d)
eafp_method(d)

p = Person()
quack_and_fly(p)
duck_typing(p)
quack_and_fly_1(p)
eafp_method(p)

# combining both together

person = {"name": "Srikar", "age": 23, "gender": "M"}
person = {"name": "Srikar"}

# LBYL (non-pythonic)

if "name" in person and "age" in person and "gender" in person:
    print('My name is {name} and I\'m a {age} year old {gender}'.format(**person))
else:
    print('Missing some keys')

# PYTHONIC  

try:
    print('My name is {name} and I\'m a {age} year old {gender}'.format(**person))
except KeyError as e:
    print(f'Missing key {e}')