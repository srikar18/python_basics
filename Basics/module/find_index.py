print("Importing find index module")

def findIndex(iterable,search):
    '''finds index of search in the iterbale'''
    for i,value in enumerate(iterable):
        if search == value:
            return i

    return -1
