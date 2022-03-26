# https://youtu.be/ajrtAuDg3yw
my_list = [0,1,2,3,4,5,6,7,8,9]

# [start:stop:step], start is inclusive and end is exclusive
    # start defaults to 0
    # end defaults to end index
    # step defaults to 1
    # start and stop can be negative, their range is
        # start --> (length * -1)
        # end --> -1
    # step can be negative i.e traverse in reverse order

# first 5 indices
print(my_list[0:5])

# incidces fron 3 to 7
print(my_list[3:8])

# indices 1 to 7
print(my_list[1:8]) # both positive
print(my_list[-9:8]) # start negative
print(my_list[1:-2]) # end negative
print(my_list[-9:-2]) # both negative

# even indices
print(my_list[::2])

# odd indices
print(my_list[1::2])

# reverse
print(my_list[::-1])

# even numbered indices in reverse
print(my_list[-2:0:-2])

# odd numbered indices in reverse
print(my_list[::-2])


# EXERCISE
sample_url = 'http://coreyms.com'
print("URL is",sample_url)

# url in reverse
print("URL in reverse is",sample_url[::-1])

# top level domain
print("Top level domain is",sample_url[-3::])

# url without http
print("URL without http is",sample_url[7::])

# url without top level domain and http
print("URL without http and top level domain is",sample_url[7:-4])
