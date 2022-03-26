# https://youtu.be/bD05uGo_sVI
# https://towardsdatascience.com/cpython-internals-how-do-generators-work-ba1c4405b4bc
# performance and memory comparision - list vs generator

# SAMPLE OUTPUT FOR LIST
    # Memory before execution [43.640625]Mb
    # List execution of order 1000000 took 0.80958223 seconds
    # Memory after execution [313.140625]Mb

# SAMPLE OUTPUT FOR GENERATOR
    # Memory before execution [43.984375]Mb
    # Generator execution of order 1000000 took 0.00000095 seconds
    # Memory after execution [44.015625]Mb

import random
import time
import memory_profiler

names = ['John Doe', 'Dave Smith', 'Mary Jacobs', 'Jane Stuart', 'Tom Wright', 'Steve Robinson', 'Nicole Jacobs', 'Jane Wright', 'Jane Doe', 'Kurt Wright', 'Kurt Robinson', 'Jane Jenkins', 'Neil Robinson', 'Tom Patterson', 'Sam Jenkins',
         'Steve Stuart', 'Maggie Patterson', 'Maggie Stuart', 'Jane Doe', 'Steve Patterson', 'Dave Smith', 'Sam Wilks', 'Kurt Jefferson', 'Sam Stuart', 'Jane Stuart', 'Dave Davis', 'Sam Patterson', 'Tom Jefferson', 'Jane Stuart', 'Maggie Jefferson']


def people_list(num):
    people = []
    for i in range(num):
        people.append({
            "_id": i,
            "name": random.choice(names),
            "age": random.randint(1, 70)
        })
    return people


def people_generator(num):
    for i in range(num):
        yield({
            "_id": i,
            "name": random.choice(names),
            "age": random.randint(1, 70)
        })


print("Memory before execution {}Mb".format(memory_profiler.memory_usage()))


# order = 10**6
# start = time.time()
# p1 = people_list(order)
# end = time.time()
# print("List execution of order {} took {:.8f} seconds".format(order, end-start))
# print("Memory after execution {}Mb".format(memory_profiler.memory_usage()))

# order = 10**6
# start = time.time()
# p1 = people_generator(order)
# end = time.time()
# print("Generator execution of order {} took {:.8f} seconds".format(order, end-start))
# print("Memory after execution {}Mb".format(memory_profiler.memory_usage()))
