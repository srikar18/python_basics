# https://youtu.be/tJxcKyFMTGo
import os

# get current working directory
print(os.getcwd())

# change working directory
os.chdir("../Basics/")
print(os.getcwd())

# list contents of directory
# fetches contents of current working directory if no argument is specified
# if provided, fetches contents of directory specified
print(os.listdir())

# create a directory
# use makedirs() if you want to create nested directories
os.mkdir('./mkdir')
# remove a directory ( will work only if the directory is empty )
# use removedirs() if you want to remove nested directories
os.rmdir('./mkdir')

# rename file / directory
try:
    os.rename('../modules/to-rename.txt', '../modules/renamed.txt')
except:
    os.rename('../modules/renamed.txt', '../modules/to-rename.txt')

# get information about a file or a directory
print(os.stat('../modules'))

# get file system tree structre i.e, traverse through all nested directories etc
for dirpath, dirname, filenames in os.walk(os.getcwd()):
    print(f'Current path : {dirpath}')
    print(f'Directory name : {dirname}')
    print(f'File names : {filenames}', end='\n\n')

# os.eniron will get all environment variables
print(os.environ)
# we can use os.environ.get('HOME') to get value of HOME variable
# getenv() will get the value of environment variable specified
print(os.getenv('HOME'))

# os.path.join() to form a path
print(os.path.join(os.getenv('HOME'), 'Desktop'))
