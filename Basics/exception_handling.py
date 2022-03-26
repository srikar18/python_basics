# https://youtu.be/NIWwJbo-9_8

# exception handling is useful to know about erros that caused the breakage
# show appropriate error messages, instead of language generated one

# open a file that does not exists
try:
    f = open('notpresent.txt')
    print('Will I run?')
except FileNotFoundError as err:
    print(err)
else:
    print('Will this run? NO -> Only when no exception occurs')
finally:
    print('Will always run')

# we can add more except statements to handle other errors
# make sure to have more specific ones at the top
# i.e, FileNotFoundError should come before Exception
# otherwise, the generic ones will always be caught without reaching the specific ones

try:
    f = open('regex_data.txt')
except FileNotFoundError as err:
    print(err)
else:
    f.close()
    print('No exception occured')
finally:
    print('Will always run')

print(f.closed)

# we can manually raise an exception using raise keyword
 