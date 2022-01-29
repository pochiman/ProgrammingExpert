##### Pairs Sum To Target #####
# Write a function that accepts two lists (list1 and list2) of integers and a target integer named target.
# Your function should return all pairs of indices in the form [x, y] where list1[x] + list2[y] == target.
# In other words, return the pairs of indices where the sum of their values equals target.

# list1 and list2 will always have the same number of elements and you may return the pairs in any order.

##### Sample Input 1 #####
# list1 = [1, -2, 4, 5, 9]
# list2 = [4, 2, -4, -4, 0]
# target = 5

##### Sample Output #####
# [
#   [0, 0],  # list1[0] = 1, list2[0] = 4, 1 + 4 = 5
#   [3, 4],  # list1[3] = 5, list2[4] = 0, 5 + 0 = 5
#   [4, 2],  # list1[4] = 9, list2[2] = -4, 9 + -4 = 5
#   [4, 3]   # list1[4] = 9, list2[3] = -4, 9 + -4 = 5
# ]

def pairs_sum_to_target(list1, list2, target):
    pairs = []

    for i, value1 in enumerate(list1):
        for j, value2 in enumerate(list2):
            if value1 + value2 == target:
                pairs.append([i, j])

    return pairs