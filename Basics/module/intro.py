# https://youtu.be/CqvZ3vGoGs0
import find_index
import sys
import os

# VARIANT ONE
# to give an alias to a module, use the following syntax
# import find_index as fi
# the above syntax allows you to use fi throght code instead of find_index
# example, fi.findIndex()

# VARIANT TWO
# to import a specific function from a module ( only gives access to that function and nothing else )
# from find_index import findIndex
# from find_index import * => will import everything 
# example, findIndex()

# VARIANT THREE
# import specific function with an alias
# from find_index import findIndex as fi
# example, fi()

courses = ['Maths','Physics','Chemistry','C','Java','Python']
print(find_index.findIndex(courses,'Mathss'))

# when you import a module, python will check for the module in the following paths
print(sys.path)
print(os.__file__) # tells where the underlying module is located
