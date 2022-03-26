# https://youtu.be/swU3c34d2NQ

# inner function has access to variabes of enclosed scope
# even after outer function execution is complete

def outer():
    message = 'Hello, there'

    def inner():
        print(message)
    return inner


my_func = outer()
# here, outer function execution is complete
# even though message is part of outer function and its execution is complete
# inner will still have access to it, because of closures
my_func()


def multiply(a):
    def calc(b):
        print(a*b)
    return calc


multiply_by_2 = multiply(2)
multiply_by_5 = multiply(5)

multiply_by_2(10)
multiply_by_5(7)
