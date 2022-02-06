##### *Args and **Kwargs #####

# Write a function named get_args_and_kwargs that accepts an unlimited number of positional and keyword 
# arguments.  The function should return True if there are at least 4 total arguments and if the keyword 
# argument num exists, is a number and is larger than 5.  Otherwise, it should return False.

# Your function should handle any errors that may occur.

##### Sample Output #####
# >>> get_args_and_kwargs("a", [2], 3, num=4)
# False
# >>> get_args_and_kwargs("a", [2], 3, num=6)
# True
# >>> get_args_and_kwargs("a", [2], num=6, x=True)
# True
# >>> get_args_and_kwargs(2, 3, a=1, b=2, num="6")
# False
# >>> get_args_and_kwargs(2, 3, a=1, b=2, number=7)
# False

def get_args_and_kwargs(*args, **kwargs):
    number_of_args = len(args) + len(kwargs)
    num = kwargs.get("num", 0)

    if not isinstance(num, int) and not isinstance(num, float):
        return False

    return number_of_args >= 4 and num > 5