# https://youtu.be/vTX3IwquFkc
person = { 'name' : 'Srikar', 'age' : 23}

# concatenation
sentence_1 = "My name is " + person['name'] + " and I'm " + str(person['age']) + " years old"
print(sentence_1)

# formatting 1 -> replace with the order in which arguments are passed
sentence_2 = "My name is {} and I'm {} years old".format(person['name'],person['age'])
print(sentence_2)

# formatting 2 -> numbering of placeholders
sentence_3 = "My name is {0} and I'm {1} years old".format(person['name'],person['age'])
print(sentence_3)

# formatting 3
sentence_4 = "My name is {name} and I'm {age} years old".format(name = person['name'],age = person['age'])
print(sentence_4)

# formatting 4
sentence_5 = "My name is {0[name]} and I'm {0[age]} years old".format(person)
print(sentence_5)

# fstring
sentence_6 = f"My name is {person['name']} and I'm {person['age']} years old"
print(sentence_6)

# NUMBER FORMATTING

# pad zeroes 
for i in range(1,11):
    print("The current value of i is {:01}".format(i))

# round to 2 decimal places
num = 3.142345
print("{0} rounded to 2 decimal places is {0:.2f}".format(num))

# commas for numbers
large_num = 1000**3
print("{0} with commas is {0:,}".format(large_num))

# DATE FORMATTING

import datetime
my_date = datetime.datetime(2022,1,1,12,15,45)

print(my_date)

# format as January 01, 2022
print("{d:%B} {d:%d}, {d:%Y}".format(d = my_date))

# format as January 01, 2022 fell on Saturday
print("{d:%B} {d:%d}, {d:%Y} fell on {d:%A}".format(d = my_date))



