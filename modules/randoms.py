# https://youtu.be/KzqSDvzOFNA
import random
from secrets import choice

# generates a random number in the range [0,1)
print("Generated using random.random() : {}".format(random.random()))

# generates a random number in the range [a,b]
print("Generated using random.uniform(1,10) : {}".format(random.uniform(1, 10)))

# generates a random integer in the range [a,b]
print("Generated using random.randint(1,10) : {}".format(random.randint(1, 10)))

# generates a random value from the list
choices = ['Hey', 'Hello', 'Hi', 'Hola', 'Namaste']
print('{}, Srikar'.format(random.choice(choices)))

# generate randomly n times
print('5 randomly generated numbers from list : {}'.format(
    random.choices(choices, k=5)))

# generate randomly n times by assigning weights to each item
# higher the weight, higher is the probability of the number getting picked up
print('Randomly generated with weights assigned to items : {}'.format(
    random.choices(choices, weights=[10, 10, 4, 4, 20], k=5)))

#  shuffle list in place
deck = list(range(1, 53))
print(f"Before shuffling {deck}")
random.shuffle(deck)
print(f"After shuffling {deck}")

# generate n unique random numbers from list
print('5 unique randomly generated numbers are {}'.format(random.sample(deck, k=5)))
