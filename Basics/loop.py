# https://youtu.be/6iF8Xb7Z3wQ
numbers = [1,2,3,4,5]

# for loop
for num in numbers:
    print(num)

# break statement -> break loop when a condition is met
print("\nBREAK STATEMENT")
for num in numbers:
    if num == 3:
        print("Found 3!!")
        break
    print(num)

# continue statement -> breaks out of current iteration and goes to next iteration
print("\nCONTINUE STATEMENT")
for num in numbers:
    if num == 3:
        print("Found 3!!")
        continue
    print(num)

# nested loop
print("\nNESTED LOOP")
for num in numbers:
    for letter in 'abc':
        print(num,letter)

# range(start,stop,step) generates numbers
    # by default starts at 0
    # by default step is 1
    # start is inclusive and stop is exclusive
print("\nEVEN NUMBERS USING RANGE")
for i in range(0,11,2):
    print(i)

# while loop -> keeps looping until condition is not met or break statement is executed
print("\nWHILE LOOP")
i = 0
while i < 10:
    print(i)
    i += 1 # IMPORTANT. If not included, condition is always met and goes into infinte loop

j = 0

print("\nExecute WHILE until a condition is met")
while True:
    print(j)
    if j == 5:
        break
    j += 1

