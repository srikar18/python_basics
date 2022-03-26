# https://youtu.be/k9TUPpGqYTo
# STRING

message = "Hello there, Srikar"
print(message)

##message_1 = "Hello there, my name's Srikar"
##print(message_1)
##
##message_2 = '''Hello there, how's you?'''
##print(message_2)
##
##multiline = '''Hello there 
##second line'''
##print(multiline)

# get length of string
print("Length of string",message,"is",len(message))

# access character at a location
print("First character of",message,"is",message[0])

# range of characters [start:end] => start is inclusive and end is exclusive
# start defaults to 0
# end defaults to end of string
print("First 5 characters of",message,"are",message[0:5])
print("First 5 characters of",message,"are",message[:5])
print("Message is",message[0:])

# STRING METHODS

# convert string to lower case
print("Lower case string is",message.lower())

# convert string to upper case
print("Lower case string is",message.upper())

# count number of characters in a string
print("Number of occurences of s in",message,"is",message.count('e'))

# find index
    # returns -1 if index is  not present
    # else first matching index
print("Index of l is",message.find('l'))

# replace character(s)
    # does not change the string in place, but rather retuns a new string
print("Replaced string is",message.replace("Srikar","Kalyan"))

# concatenation method one
name = 'Srikar'
age = '23'
intro_1 = "Hello, I'm " + name.upper() + " and I'm " + age + " years old"
print(intro_1)

# concatenation method two
intro_2 = "Hello, I'm {} and I'm {} years old".format(name.upper(),age)
print(intro_2)

# fstrings - concatenation method three (only for python 3.6 or greater)
intro_3 = f"Hello, I'm {name.upper()} and I'm {age} years old"
print(intro_3)


