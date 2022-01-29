# Write the function string_lengths(strings), which takes in a list of strings and returns a new list containing 
# the lengths of the strings, in their relevant order.  You can assume that strings will only contain strings.

##### Sample Output #####
# >>> strings = ["hello", "this", "is", "a", "beard", "orange", "blue"]
# >>> string_lengths_list = string_lengths(strings)
# >>> print(string_lengths_list)
# [5, 4, 2, 1, 5, 6, 4]

def string_lengths(strings):
    lengths = []

    for string in strings:
        length = len(string)
        lengths.append(length)

    return lengths