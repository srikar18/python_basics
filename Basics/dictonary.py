# https://youtu.be/daefaLgNkw0
student = { 'name': 'Srikar', 'age': 23, 'courses': ['Maths','Chemistry']}
print(student)

# access certain key in a dictonary
    # throws an error if key doesn't exist
print(f"Name is {student['name']}")

# get method of dictonary is same as above, except it retuns None when key doesn't exist
try:
    print(student['sports']) # throws KeyError
except:
    print("Exception occured")

print(student.get('sports')) # returns None
print(student.get('sports','Cricket')) # return second argument as default value

# add a new key to the dictonary
student['sports'] = ['Cricket']

# update exisiting key
student['courses'] = []

print(student)

# use update method to update multiple things at once
student.update({'courses': ['C','C++','Java'], 'sports': ['Cricket','Badminton']})
print(student)

# delete a key in the dictonary
del student['sports']
print(student)

# we can also use pop() to remove a key
student.pop('courses')
print(student)

# length of dictonary
print(len(student))

# get all the keys of a dictonary
print(student.keys())

# get all the values of a dictonary
print(student.values())

# get all key/value pairs of a dictonary
print(student.items())

# looping over a dictonary

for key,value in student.items():
    print(key,value,sep=" --> ")
