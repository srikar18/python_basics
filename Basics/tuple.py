# https://youtu.be/W8KRzm-HUcc
# cannot modify a tuple, once it's created i.e, immutable
# lists are mutable and tuples are immutable

# EMPTY TUPLE
empty_tuple_1 = tuple()
print(empty_tuple_1)
empty_tuple_2 = ()
print(empty_tuple_2)

# MUTABLE
list_1 = [1,2,3,4,5]
list_2 = list_1

list_1[0] = 0
print(list_1)
print(list_2)

# IMMUTABLE
tuple_1 = (1,2,3,4,5) 
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuples have similar methods to that of a list (excluding ones which cause muation like pop, append etc)


