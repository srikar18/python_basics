# https://youtu.be/QVdf0LgmICw
# LEGB
# Local, Enclosing, Global, Built-in
# scope refers to where our variables can be accessed from

x = 'global x'

def test():
    # to tell python we want to use global x, use the below line (even if x is declared locally)
    # global x
    x = 'local x'
    print(x) # prints local x if x is declared within function, else prints global x


test()
print(x)

# built in scope - min(), max() etc which are provided by Python
# be careful, even if we override them Python does not throw any error

# enclosing scope
    # check if there is anything in local scope
    # if no, go to enclosing scope
    # in this case, if x is not declared inside inner function
    # it will look in enclosing scope i.e, outer function scope
    # only if x is not found in enclosing scope, it looks at global scope

def outer():
    x = 'outer x'

    def inner():
        # if you want to change outer x, use nonlocal
        # nonlocal x -> will give access to x of outer function
        x = 'inner x' 
        print(x)
    inner()
    print(x)

outer()
