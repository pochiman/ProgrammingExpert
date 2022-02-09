##### Print Return Value Decorator #####

# Write a decorator function named print_return_value that prints the return value of any function 
# it decorates.  Your decorator should work on any function, regardless of the number of parameters.

def print_return_value(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        print(return_value)
        return return_value

    return wrapper