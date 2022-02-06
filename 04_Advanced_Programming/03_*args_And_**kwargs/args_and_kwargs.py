# def sum_items(*args, **kwargs):
#   print(sum(args))
#   print(args)
#   print(kwargs)
# print(kwargs['k'])

# sum_items(1, 2, 3, k=2, a=2)
# sum_items(1, 2, 3, 4)
# sum_items(1)
# sum_items()

########## ########## ########## ########## ##########

# def sum_items(a, b, c):
#   print(a, b, c)
#   return a + b + c

# args = [4, 5, 7]
# args = (4, 5, 7)
# args = "457"
# x = sum_items(args[0], args[1], args[2])
# kwargs = {"a": 5, "c": 10, "b": 5}
# x = sum_items(*args)
# x = sum_items(a = 2, c = 4, b = 5)
# x = sum_items(**kwargs)
# print(x)

########## ########## ########## ########## ##########

# def sum_items(p1, p2, a=None, b=None, c=None):
#   print(p1, p2, a, b, c)
#   return a + b + c + p1 + p2

# args = [1, 2]
# kwargs = {"a": 5, "c": 10, "b": 5}
# x = sum_items(*args, **kwargs)
# print(x)

########## ########## ########## ########## ##########

# def sum_items(p1, p2, a=None, b=None, c=None):
#   print(p1, p2, a, b, c)
#   return a + b + c + p1 + p2

# values = [1, 2, 3, 4, 5, 2, 3, 1, 2, 3]

# for val in values:
#   print(val, end=", ")

# print(values)
# print(*values)

########## ########## ########## ########## ##########

def test(p1, *args, **kwargs):
  print(p1, args, kwargs)

values = [1, 2, 3, 4, 5, 6]
kwargs = {"s": 1, "hello": 4, "k": True}
test(4, *values, **kwargs)