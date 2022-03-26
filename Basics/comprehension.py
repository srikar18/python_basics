# https://youtu.be/3dt4OGnU5sM
# LIST COMPREHENSION
nums = list(range(11))
print(nums)

# I want n for n in nums

# WITHOUT LIST COMPREHENSION
my_list = []
for n in nums:
    my_list.append(n)

print(my_list)

# USING LIST COMPREHENSION
my_list = [n for n in nums]
print(my_list)

# I want n*n for n in nums

# WITHOUT LIST COMPREHENSION
my_list = []
for n in nums:
    my_list.append(n*n)

print(my_list)

# USING LIST COMPREHENSION
my_list = [n*n for n in nums]
print(my_list)

# I want n for n in nums if n is even

# WITHOUT LIST COMPREHENSION
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)

print(my_list)

# USING LIST COMPREHENSION
my_list = [n for n in nums if n % 2 ==0]
print(my_list)

# I want a letter, number pair for each letter in abcd and each number in 1234

# WITHOUT LIST COMPREHENSION
letter = 'abcd'
number = '1234'
my_list = []
for l in letter:
    for n in number:
        my_list.append((l,n))

print(my_list)

# USING LIST COMPREHENSION
my_list = [(l,n) for l in letter for n in number]
print(my_list)

# DICTIONARY COMPREHENSION

# WITHOUT COMPREHENSION
my_dict = {}
names = ['Srikar','Kalyan','Walter','Jessie']
roll_nos = [49,12,33,18]

for (name,rno) in zip(names,roll_nos):
    my_dict[name] = rno

print(my_dict)

# WITH COMPREHENSION
my_dict = {name: rno for name,rno in zip(names,roll_nos)}
print(my_dict)

# SET COMPREHENSIONS

# WITHOUT COMPREHENSION
duplicates = [1,1,2,3,4,3,2,4,3,5,6,4,8,6,9,8,9,0]
my_set = set()

for n in duplicates:
    my_set.add(n)

print(my_set)

# WITH COMPREHENSION
my_set = {n for n in duplicates}
print(my_set)
