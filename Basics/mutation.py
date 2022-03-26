# https://youtu.be/5qQQ3yzbKp8
# An immutable object is an object whose state cannot be modified after its created
# This is in contrast to a mutable object which can be modified after its created

# IMMUTABLE -> cannot do a[0] = 'S' etc
a = 'srikar'
print("Value of a is",a,"and is located at",id(a))

a = 'kulkacherla'
print("Value of a is",a,"and is located at",id(a))

# MUTABLE
a = [1,2,3,4,5]
print("Value of a is",a,"and is located at",id(a))

a[0] = 6
print("Value of a is",a,"and is located at",id(a))

# memory problem when not programmed properly
employees = ['First','Second','Third','Fourth','Fifth']

output = '<ul>\n'

for employee in employees:
    output += '\t<li>{0}</li>\n'.format(employee)
    print("Address of output is {}".format(id(output))) # address changes everytime

output += "</ul>"
print(output)

