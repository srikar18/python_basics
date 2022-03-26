# https://youtu.be/9Os0o3wzS_I
# set of instructions packaged together to perform a specific task

def randomFunction():
    # The pass statement is useful when you don’t write the implementation of a function
    # but you want to implement it in the future.
    pass

def greetUser():
    print("Hello there, welcome!")
    # returns None if nothing is sepcified
    return "hello"

print(greetUser) # prints info about function
greetUser() # execute the function
print(greetUser()) # execute the function and print the return value of the function
 
# function with parameters
# we can provide default value to parameters which will come into affetc when no 
# arguments are passed to the function
# if you call a function (without default values) without arguments, it will throw an error
def greetUserWithName(name='User'):
    return f"Hello there, {name}. Hope you have a great day!!"

greeting = greetUserWithName('Srikar')
print(greeting)
print(greetUserWithName())

# args and kwargs
# not necessary to name them args and kwargs, but it's a convention

# In a function call, keyword arguments must follow positional arguments.
# All the keyword arguments passed must match one of the arguments
# accepted by the function.No argument may receive a value more than once.
    # https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

student_info('Srikar','Male',age=23,surname='K')

courses = ['Hindi','English']
student = { "name": "Srikar", "age": 23}

# unpacks values and sends them to the function
    # *courses will pass Hindi and English
    # **student will pass name='Srikar' and age=23
student_info(*courses,**student)


daysMap = {
    "January":31,
    "February":28,
    "March":31,
    "April":30,
    "May":31,
    "June":30,
    "July":31,
    "August":31,
    "September":30,
    "October":31,
    "November":30,
    "December":31
}

def getDaysInAMonth(month='January'):
    # doc strings -> tell what the function does
    """this function returns the number of days in a month"""
    return daysMap.get(month)

print(getDaysInAMonth('December'))

# to print doc strings for the function

help(getDaysInAMonth) # opens man page like view
print(getDaysInAMonth.__doc__) # prints doc string
