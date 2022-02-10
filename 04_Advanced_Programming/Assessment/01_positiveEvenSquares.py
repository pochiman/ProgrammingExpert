##### Positive Even Squares #####

# Write a function that accepts any number of positional arguments, all of which you may assume will 
# be lists of integers.  Your function should filter all of these lists such that they only contain even 
# positive integers and combine all of the lists into one list of integers.  Your function should then 
# modify the combined list such that it contains the squares of all of the elements and return that list.

# Use a combination of the map, filter and lambda functions/keywords to modify the lists.

# See the sample input for an example.

##### Sample Input 1 #####
# *args = [[-5, 2, 3, 4, 5], [1, 3, 5, 6, 7], [-9, -8, 10]]
# arguments will be passed positionally to the function like this:
# positive_even_squares([-5, 2, 3, 4, 5], [1, 3, 5, 6, 7], [-9, -8, 10])

##### Sample Output 1 #####
# The combined list of positive even integers is: [2, 4, 6, 10], 
# [4, 16, 36, 100] the result is the squares of all of these values.

def positive_even_squares(*args):
    positive_even_nums = []

    for lst in args:
        filtered_list = filter(lambda x: x > 0 and x % 2 == 0, lst)
        positive_even_nums.extend(filtered_list)

    squares = map(lambda x: x ** 2, positive_even_nums)
    return list(squares)