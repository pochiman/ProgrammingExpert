# lst = [2, 1, 3, 4, 2, 3, 2, 1]
# lst = (2, 1, 3, 4, 2, 3, 2, 1)
# print(lst.sort())
# print(sorted(lst))
# lst.sort(reverse=True)
# print(sorted(lst, reverse=True))
# print(tuple(sorted(lst, reverse=True)))
# print(lst)

########## ########## ########## ########## ##########

# lst = [[1, 2], [3, 4], [5, 6], [-1, -2], [0, 0]]
# lst = [[1, -2], [3, -4], [5, -6], [-1, -2], [0, 0]]
# lst.sort()
# print(lst)

########## ########## ########## ########## ##########

def sort_second_index(item):
  # return item[1]
  return sum(item)

lst = [[1, -2], [3, -4], [5, -6], [-1, -2], [0, 0]]
# lst.sort(reverse=True, key=sort_second_index)
# lst.sort(key=sort_second_index)
new_list = sorted(lst, key=sort_second_index)
# print(lst)
print(new_list)