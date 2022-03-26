# https://youtu.be/W8KRzm-HUcc
# unordered collection of data without any duplicates

# EMPTY SET
empty_set = set()
print(empty_set)


courses = {'Maths','Physics','Chemistry','Hindi','English','History'}
important_courses = {'Maths','Biology','Chemistry'}
print(courses)

# sets are optimized for membership tests
print('Maths' in courses)
print('Telugu' in courses)

# union of sets
print(courses.union(important_courses))

# intersection of sets
print(courses.intersection(important_courses))

# present in A but not B =>   A.difference(B) i.e, A - (A n B)
print(courses.difference(important_courses))

