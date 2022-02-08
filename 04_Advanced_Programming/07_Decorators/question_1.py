##### Add One Decorator #####

# Write a decorator function named add_one that simply adds one to the return value of 
# any function it decorates.  Then use this function to decorate the add_values function.

# You may assume the arguments passed to add_values will always be integers.

##### Sample Output #####
# >>> add_values(2, 2)
# 5

##### Solution 1 #####
# def add_one(func):
#     def wrapper(x, y):
#         return_value = func(x, y)
#         return return_value + 1

#     return wrapper


# @add_one
# def add_values(x, y):
#     return x + y

##### Solution 2 #####
def add_one(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        return return_value + 1

    return wrapper


@add_one
def add_values(x, y):
    return x + y