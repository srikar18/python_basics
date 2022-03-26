# https://youtu.be/K8L6KVGG-7o

# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# does match second Ha in HaHa as it does not have a word boundar
# it is a part of the string
# word boundary checks for spaces or new line charcs or tabs

pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# searches for phone numbers in the file
# starting with 800 or 900

with open('./regex_data.txt') as rf:
    pattern = re.compile(r'[89]00-\d{3}-\d{4}')
    matches = pattern.finditer(rf.read())
    for match in matches:
        print(match)

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9-.]+@[a-zA-Z0-9\-]+\.(com|net|edu)')
matches = pattern.finditer(emails)

for match in matches:
    print(match)

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# perform a case sensitive match
pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)', re.IGNORECASE)
matches = pattern.finditer(urls)

# group() method contains the matched group
# group(0) will have the entire matched str
for match in matches:
    print(match.group(2), match.group(3))

# we can also use sub method to extract out matches
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)
