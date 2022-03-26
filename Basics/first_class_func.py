# https://youtu.be/kr0mpwqttM0

#  When you say that a language has first-class functions, it means that the language
# treats functions as values – that you can assign a function into a variable, pass it around etc.

# a higher order function is a function that accepts other functions as arguments
# or returns a function

# function which accpets another function as an argument
def my_map(func, lov):
    res = []
    for n in lov:
        res.append(func(n))
    return res


squares = my_map(lambda a: a * a, [1, 2, 3, 4, 5])
print(squares)

# function which returns a function


def cal_exponent(a):
    def multiplier(n):
        return a**n
    return multiplier


a = cal_exponent(5)
print(a(2))


def html_tag(tag):
    def wrap_text(msg):
        return f'<{tag}>{msg}</{tag}>'
    return wrap_text


print_h1 = html_tag('h1')
print(print_h1('Hello there'))
