# https://youtu.be/D3JvDWO-BY4

# By default sort in performed in ascending order
# pass reverse = True, to sort in descending order

# sorted() function retuns a new list

# sort() method is applicable only for LISTS
# to sort the list in place use li.sort(). Return value is None

# LIST

from operator import attrgetter

li = [3, 6, 1, 4, 8, 7, 9, 0, 2, 5]
s_li = sorted(li)
print(f'Sorted list is {s_li}')
print(f'Original list is {li}')

li.sort(reverse=True)
print(f'List reverse sorted in place is {li}')

# TUPLE
tu = (3, 6, 1, 4, 8, 7, 9, 0, 2, 5)
s_tu = sorted(tu)
print(f'Sorted tuple is {s_tu}')
print(f'Original list is {tu}')

try:
    tu.sort(reverse=True)
    print(f'Tuple reverse sorted in place is {tu}')
except:
    print("Not supported for tuple")

# for a dictionary only the keys are sorted

# sorting for Classes


class Employee():
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self) -> str:
        return f'({self.name},{self.age},{self.gender})'


e1 = Employee('Srikar', 24, 'Male')
e2 = Employee('Kalyan', 23, 'Male')
e3 = Employee('Walter', 44, 'Male')

employees = [e1, e2, e3]
def emp_sort(emp): return emp.name


s_employees = sorted(employees, key=emp_sort)
print(s_employees)

# using lambda function
s_employees = sorted(employees, key=lambda a: a.name)
print(s_employees)

# using attrgetter
s_employees = sorted(employees, key=attrgetter('name'))
print(s_employees)
