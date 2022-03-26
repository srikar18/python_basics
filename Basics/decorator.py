# https://youtu.be/FsAPt_9Bf3U

def decorator_function(operation):
    def wrapper_function():
        print('Wrapper function executed before {}'.format(operation.__name__))
        return operation()
    return wrapper_function

@decorator_function
def say_hello():
    print('Hello there!')

say_hello()

# the above syntax which is sugar-coated means the same as below

# say_hello = decorator_function(say_hello)
# say_hello()

