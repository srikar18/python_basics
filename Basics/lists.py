# https://youtu.be/W8KRzm-HUcc
# EMPTY LIST
empty_list_1 = list()
print(empty_list_1)
empty_list_2 = []
print(empty_list_2)

courses = ['Maths','Physics','Chemistry','Biology','English']

print(courses)


# length of list
print("You've got",len(courses),"courses")

# indexed from 0 to len(list) - 1 (OR) len(list) * -1 to -1
# use list[index] to get particular item in list at certain index

print("First course is",courses[0])
print("First course is",courses[-5])

# add an item to tne end of the list
courses.append('Arts');
print(courses)

# insert an item at ap articular index
courses.insert(0,'Biology')
print(courses)

# extending lists -> adds items of a list at end of another list
courses_2 = ['Telugu','Hindi']
courses.extend(courses_2)
print(courses)

# remove ceratin value in the list
    #  only the first matched is removed
    #  throws an error if no match is found
courses.remove('Hindi')
print(courses)


# remove last item of index and return it
    # specify index number to remove item at certain position
print("Popped out course is",courses.pop())

# reverses a list in place and returns None
courses.reverse()
print("Reverse list is",courses)

# sort a list (by default in ascending)
numbers = [4,9,11,8,6]
numbers.sort()
print("Sorted list is",numbers)

# to sort in reverse order, pass reverse=True as an argument to the function
numbers.sort(reverse=True)
print("Reverse sorted list is",numbers)

# use sorted() function to get sorted list (ascending by default)  i.e, return sorted list instead of sorting it in place
sorted_numbers = sorted(numbers) # pass reverse = True to get the list in reverse order 
print(sorted_numbers)

# minimum value in list
print("Minimum value in list is",min(numbers))

# maximum value in list
print("Maximum value in list is",max(numbers))

# sum of values in list => only works in items are integer or float type
print("Sum of values in list is",sum(numbers))

# find index of a certain value
    # returns the first matched index
    # throws an error if value does not exist
course_num = courses.index('Maths');
print("Maths is your",course_num,"course")

# check for a value in the list
print('Arts' in courses)
print('Sanskrit' in courses)

# loop over list using "in"
print("\n***** LOOP *****\n")
for course in courses:
    print(course)

# loop over list using "in" and also get indixes during each iteration
print("\n")
for index,course in enumerate(courses):
    print(index,course,sep=" --> ")

# start at certain index using enumerate
print("\n")
for index,course in enumerate(courses,start=1):
    print(index,course,sep=" --> ")

# join values of list using a separator
courses_str = ', '.join(courses)
print(courses_str)

# split down string into list using a separator
courses_list = courses_str.split(', ')
print(courses_list)










