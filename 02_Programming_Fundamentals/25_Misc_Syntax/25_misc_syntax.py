# lst = []

# for i in range(1, 11):
#   lst.append(i)

# print(lst)

########## ########## ########## ########## ##########

# lst = [i for i in range(1, 11)]
# lst = [i + 1 for i in range(1, 11)]
# lst = [i / 2 for i in range(1, 11)]
# lst = [i / 2 for i in range(1, 11) if i % 2 == 0]
# lst = [i * j for i in range(1, 11) for j in range(5)]
# lst = (i * j for i in range(1, 11) for j in range(5))
# lst = tuple([i * j for i in range(1, 11) for j in range(5)])
# print(lst)

########## ########## ########## ########## ##########

# s = {i * j for i in range(1, 11) for j in range(5)}
# s = {i: j for i in range(1, 11) for j in range(5)}
# s = {j: i for i in range(1, 11) for j in range(5)}
# print(s)

########## ########## ########## ########## ##########

# x = y = z = 2
# x, y = 1, 2
# x, y, z = (1, 2, 3)
# x, y, z = [1, 2, 3]
# print(x, y, z)
# print(x, y, z)

########## ########## ########## ########## ##########

def foo():
  """
  this is the foo function
  """
  pass

# help(foo)
# help(len)
# help(1)
help(max)