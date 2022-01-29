# Write a function named compare_lists that accepts two optional parameters, lst1 and lst2.  The function should return the number of unique 
# common elements between the two lists.  If either of the lists isn't passed as a parameter, it should be treated as an empty list.

# You can assume that the input lists will only contain integers.

##### Sample Output #####
# >>> compare_lists([1, 2, 3], [1, 1, 1])
# 1 # 1
# >>> compare_lists([1, 2, 3], [1, 3, 1])
# 2 # 1 and 3
# >>> compare_lists([1, 2, 3])
# 0
# >>> compare_lists(lst2=[1, 1, 1])
# 0

##### Solution 1 #####
# def compare_lists(lst1=[], lst2=[]):
#     lst1_set = set(lst1)
#     lst2_set = set(lst2)
#     set_intersection = lst1_set.intersection(lst2_set)

#     return len(set_intersection)

##### Solution 2 #####
# def compare_lists(lst1=[], lst2=[]):
#     lst1_set = set(lst1)
#     lst2_set = set(lst2)

#     set_intersection_length = 0
#     for num in lst1_set:
#         if num in lst2_set:
#             set_intersection_length += 1

#     return set_intersection_length

##### Solution 3 #####
def compare_lists(lst1=[], lst2=[]):
    lst1_set = set(lst1)

    set_intersection_length = 0
    for num in lst2:
        if num in lst1_set:
            set_intersection_length += 1
            lst1_set.remove(num)

    return set_intersection_length