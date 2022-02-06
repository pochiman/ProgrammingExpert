##### Lambda Functions #####

# Write the following lambda functions.

##### A lambda function that takes three integer or float parameters and returns their sum.
##### You should store this lambda function in the variable add_values.

##### A lambda function that takes two string parameters and returns the maximum of their lengths.
##### You should store this lambda function in the variable max_length.

##### A lambda function that takes two list parameters and returns a set containing the elements 
##### from both lists.  You should store this lambda function in the variable create_set.

##### Sample Output #####
# >>> add_values(3, 4, 5)
# 12
# >>> max_length("hello", "tim")
# 5
# >>> create_set([1, 2, 3, 4], [2, 3, 5])
# {1, 2, 3, 4, 5}

##### Solution 1 #####
# add_values = lambda x, y, z : x + y + z

# max_length = lambda x, y: max(len(x), len(y))

# create_set = lambda x, y: set(x).union(y)

##### Solution 2 #####
# add_values = lambda x, y, z : sum([x, y, z])

# max_length = lambda x, y: max(len(x), len(y))

# create_set = lambda x, y: set(x + y)

##### Solution 3 #####
add_values = lambda x, y, z : sum([x, y, z])

max_length = lambda x, y: max(len(x), len(y))

create_set = lambda x, y: set(x) | set(y)