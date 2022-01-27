# def print_value():
#   print("hello")

# print_value()

########## ########## ########## ########## ##########

# def print_value(value):
#   print(value)

# print_value("hi")
# print_value("1")
# print_value("True")

########## ########## ########## ########## ##########

# def add_5(x, y, z):
#   result = x + y + z + 5
#   # print(result)
#   return result

# x = 4
# y = 5
# z = 6

# # add_5(5, 5, 2)
# r = add_5(x, y, z)
# print(r)

########## ########## ########## ########## ##########

# def get_negative_sum(x, y, z):
#   result = x + y + z
#   if result < 0:
#     return result

#   return 1  

# x = -4
# y = -5
# z = -6
# # z = 100

# r = get_negative_sum(x, y, z)
# print(r)

########## ########## ########## ########## ##########

# def new_range(start, stop):
# def new_range(start=0, stop=10):
# def new_range(start, stop):
# def new_range(stop, start=0):
#   x = start

#   while x < stop:
#     print(x)
#     x += 1

# new_range(1, 10)
# new_range()
# new_range(5, 15)
# new_range(stop=5, start=-5)
# new_range(stop=4, start=-2)
# new_range(10)

########## ########## ########## ########## ##########

# def return_values(x, y):
#   return x + 1, y + 1

# result = return_values(1, 2)
# print(result)
# x, y = return_values(1, 2)
# print(x, y)

########## ########## ########## ########## ##########

# def remove_chars(base, chars):
# def remove_chars(base, chars=""):
#   new_string = base
#   for char in chars:
#     new_string = new_string.replace(char, "")

#   return new_string

# # result = remove_chars("hello world", "l")
# result = remove_chars("hello world", chars="lo")
# print(result)

########## ########## ########## ########## ##########

# def sum_lists(list1, list2):
#   list1_sum = sum_list(list1)
#   list2_sum = sum_list(list2)
#   return list1_sum, list2_sum

# def sum_list(lst):
#   total = 0

#   for num in lst:
#     total += num

#   return total

# sum1, sum2 = sum_lists([1, 2, 3, 4], [-1, -2, -3, -4])
# print(sum1, sum2)

########## ########## ########## ########## ##########

def sum_lists(list1, list2):
  def sum_list(lst):
    total = 0

    for num in lst:
      total += num

    return total

  list1_sum = sum_list(list1)
  list2_sum = sum_list(list2)
  return list1_sum, list2_sum

sum1, sum2 = sum_lists(list1=[1, 2, 3, 4], list2=[-1, -2, -3, -4])
print(sum1, sum2)