##### Integer Sum #####

# Write a function named integer_sum that accepts any number of positional arguments, which 
# are assumed to be integers.  This function should return the sum of all of these integers.

# To handle invalid input (arguments that are not integers), you must write the following 
# decorators and use them to decorate the integer_sum function.

##### flatten_lists: this decorator should flatten any list arguments for the decorated 
##### function by extracting their elements and passing them as individual arguments instead 
##### of the list.  For example, if [1, 2, True] is an argument, then 1, 2 and True should be 
##### extracted and passed as arguments instead of the list to the decorated function.

##### convert_strings_to_ints: this decorator should convert any string arguments that are 
##### valid integers to integers and pass them to the decorated function.  Any string that 
##### is not a valid integer should be removed as an argument to the decorated function.

##### filter_integers: this decorator should remove any argument that is not an integer and 
##### call the decorated function with only integer arguments.

##### You may assume all arguments passed to integer_sum will be of type float, int, str or list.

##### Sample Input 1 #####
# args = ["1", "2", -0.9, 4, [5, "hi", "3"]]
# arguments will be passed positionally to the function like this: integer_sum(1, 2, 4, 5, 3)

##### Sample Output 1 #####
# 12  # the sum of "1", "2", 4 and 5.
      # Note: the "3" inside of the last list argument should not be converted to an integer.

def flatten_lists(func):
    def wrapper(*args):
        new_args = []
        for arg in args:
            if isinstance(arg, list):
                new_args.extend(arg)
            else:
                new_args.append(arg)

        result = func(*new_args)
        return result

    return wrapper


def convert_strings_to_ints(func):
    def wrapper(*args):
        new_args = []
        for arg in args:
            if isinstance(arg, str) and arg.isdigit():
                new_args.append(int(arg))
            else:
                new_args.append(arg)

        result = func(*new_args)
        return result

    return wrapper


def filter_integers(func):
    def wrapper(*args):
        new_args = []
        for arg in args:
            if isinstance(arg, int):
                new_args.append(arg)

        result = func(*new_args)
        return result

    return wrapper


@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)