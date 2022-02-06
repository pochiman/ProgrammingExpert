# lst = [1, 2, 3, 4, 5, 6, 7]
# new_lst = map(lambda x: x ** 2, lst)
# new_lst = list(map(lambda x: x ** 2, lst))
# print(new_lst)

# for el in new_lst:
#   print(el)

########## ########## ########## ########## ##########

# import math

# lst = [1, 2, 3, 4, 5, 6, 7]
# new_lst = list(map(lambda x: math.sqrt(x), lst))
# print(new_lst)

########## ########## ########## ########## ##########

# import math

# lst = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]
# new_lst = list(map(lambda x: sum(x), lst))
# print(new_lst)

########## ########## ########## ########## ##########

# import math

# lst = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]

# new_lst = filter(lambda x: sum(x) > 6, lst)
# new_lst = list(filter(lambda x: sum(x) > 6, lst))
# new_lst = list(filter(lambda x: True, lst))
# new_lst = list(filter(lambda x: False, lst))
# new_lst = list(filter(lambda x: len(x) > 2, lst))
# print(new_lst)

# for el in new_lst:
#   print(el)

########## ########## ########## ########## ##########

import math

lst = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]

new_lst = filter(lambda y: y % 2 == 0, map(lambda x: sum(x), lst))
print(list(new_lst))