# https://youtu.be/Uh2ebFW8OYM

# r - read
# w - write
# a - append
# r+ - read and write

# NOT RECOMMENDED
# we have to explicitly close the files, failure to do so results in memory leaks
# pass the path of the file to open
f = open('test.txt', 'r')
print("Opened {} in {} mode".format(f.name, f.mode))
f.close()
print(f.closed)

# use context manager to avoid explicit closing of file
# files are automatically closed when wth block is complete
# we have access to f variable outside of with block , but file would be closed by then
with open('test.txt', 'r') as f:
    print("Opened {} in {} mode".format(f.name, f.mode))

    # read entire file content
    f_contents = f.read()
    print(f_contents)

    # use f.tell to know where the pointer is
    print(f.tell())

    # set pointer to starting of file
    # as file is already read, below will not produce any result
    f.seek(0)

    # read lines in a file
    f_lines = f.readlines()
    print(f_lines)

    f.seek(0)
    # f.readline() reads one line per call
    # below loop uses readline() internally
    for line in f:
        print(line, end='')

    print("*"*10)
    f.seek(0)
    size_to_read = 10
    # pass numbers of charcters to read
    # will return empty string once EOF is reached
    f_read = f.read(size_to_read)

    while(len(f_read) > 0):
        print(f_read, end='')
        # print('Position in file is {}'.format(f.tell()))
        f_read = f.read(size_to_read)

print(f.closed)

# WRITING TO A FILE
try:
    with open('test.txt', 'r'):
        f.write()
except:
    print("Cannot write to a file opened in read mode")

print(f.closed)

# will create a file if it doesn't exist
# will override the contents of file if already present
# if you do not want to override, open the file in append mode

with open('test2.txt', 'w') as f:
    f.write("test2..")

# copy contents of one file to another
# can have both of them in a single line
# with open('test.txt','r') as rf, open('test_copy.txt','w') as wf

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        file_contents = rf.read()
        wf.write(file_contents)

# copy images
with open('reigen.jpg', 'rb') as ir, open('reigen_copy.jpg', 'bw') as iw:
    iw.write(ir.read())
