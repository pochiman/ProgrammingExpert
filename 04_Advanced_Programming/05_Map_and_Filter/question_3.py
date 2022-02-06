##### Map And Filter #####

# Use the map and filter functions to create an iterable that contains the even squares of all elements 
# in the lst list.  Once you've created this iterable, print out all of its values on separate lines.

# You should use lambda's for any functions you create.

##### Sample Output #####
# 4
# 16
# 36
# 64
# 100

##### Solution 1 #####
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squares = map(lambda x: x ** 2, lst)
# even_squares = filter(lambda x: x % 2 == 0, squares)

# for value in even_squares:
#     print(value)

##### Solution 2 #####
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, lst))

for value in even_squares:
    print(value)