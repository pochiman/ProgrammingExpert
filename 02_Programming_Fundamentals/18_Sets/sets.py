########## ########## ########## ########## ##########

# x = set()
# y = {}
# y = {1, 2}

# print(type(x))
# print(type(y))

########## ########## ########## ########## ##########

# x = {1, 2, 2, 1, 2, 1}

# x.add(3)
# x.remove(2)
# x.clear()

# print(x)
# print(len(x))

########## ########## ########## ########## ##########

# x = {1, 2, 2, 1, 2, 1, "hello", "4", True, 0.2, (1, 2)}

# contains = 1 in x

# print(contains)

########## ########## ########## ########## ##########

# x = {1, 2}
# y = {2, 3}
# y = {1, 2}

# z = x.union(y)
# z = x | y
# print(z)
# print(x)

########## ########## ########## ########## ##########

# x = {1, 2, 3}
# y = {1, 2, 4}

# z = x.intersection(y)
# z = y.intersection(x)
# z = y & x

# z = x.difference(y)
# z = y.difference(x)
# z = x - y
# z = y - x

# z = x.symmetric_difference(y)
# z = y.symmetric_difference(x)
# z = y ^ x
# z = x ^ y
# print(z)
# print(x)

# x.update(y)
# y.update(x)
# x.difference_update(y)
# y.difference_update(x)
# x.symmetric_difference_update(y)
# y.symmetric_difference_update(x)

# print(x)
# print(y)

########## ########## ########## ########## ##########

# x = {1, 2, 3, 8}
# x = {1, 2, 3}
# y = {1, 2, 3, 4, 5, 6, 7}

# print(x.issubset(y))
# print(y.issubset(x))
# print(y.issuperset(x))
# print(x.issuperset(y))
# print(x <= y)
# print(x >= y)
# print(y >= x)
# print(y > x)
# print(x < y)
# print(y < x)

########## ########## ########## ########## ##########

# x = [1, 2, 2, 2, 3, 4, 5, 3, 4]
# x = "hello"
# set_x = list(set(x))

# print(set_x)

########## ########## ########## ########## ##########

numbers = set()

while True:
  num = int(input("Number: "))

  if num in numbers:
    break

  numbers.add(num)