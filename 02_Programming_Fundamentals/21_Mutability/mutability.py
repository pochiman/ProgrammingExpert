##### Immutable #####
# int
# float
# str
# tuple
# bool

# x = 1
# y = x
# x += 1

# print(x, y)

########## ########## ########## ########## ##########

##### Mutable #####
# list
# set
# dict

# x = []
# y = x
# x.append(2)

# print(x, y)

########## ########## ########## ########## ##########

# x = []
# y = []
# y = x

# print(x is y)

########## ########## ########## ########## ##########

# a = 1
# b = a
# print(a is b)

# a += 1
# print(a is b)
# print(a, b)

########## ########## ########## ########## ##########

# a = 1
# b = a
# b = 2
# b = 1
# b += 1

# print(id(a), id(b))

########## ########## ########## ########## ##########

# def func(lst, x):
#   lst.append(x)
  # print(lst)

# a = []
# func(a, 2)
# func(a, 3)

# print(a)

########## ########## ########## ########## ##########

# d = {}
# d["k"] = "v"

# a = d
# a["a"] = "b"
# d["b"] = "a"

# print(d, a)
# print(d is a)

########## ########## ########## ########## ##########

# s1 = set()
# s2 = s1

# s1.add(1)
# s2.add(2)

# print(s1, s2)
# print(s1 is s2)

########## ########## ########## ########## ##########

# def func(s, x):
#   s.add(x)

# s1 = set()
# func(s1, 1)
# print(s1)

########## ########## ########## ########## ##########

# a = [1, 2, 3]
# b = a[:]

# a.append(4)
# print(a, b)
# print(a is b)

########## ########## ########## ########## ##########

# def func(lst):
#   lst = lst[:]
#   lst.append(4)

# x = [1, 2, 3]
# func(x)
# print(x)

########## ########## ########## ########## ##########

# s1 = {1, 2, 3}
# s2 = s1.copy()

# s1.add(4)
# print(s1, s2)

########## ########## ########## ########## ##########

# s1 = {"k": "v"}
# s2 = s1.copy()

# s1[1] = 2
# print(s1, s2)
# print(s1 is s2)

########## ########## ########## ########## ##########

# lst = [[1, 2, 3], [3, 4, 5]]
# lst[0].append(4)
# lst[1].append(4)

# print(lst)

########## ########## ########## ########## ##########

# lst = [1, 2, 3]
# d = {1: lst}

# lst.append(4)
# print(d)

########## ########## ########## ########## ##########

# d = {1: [1, 2, 3]}

# d[1].append(4)
# print(d)

########## ########## ########## ########## ##########

# x = 2
# d = {1: x}

# x = 3
# print(d)

########## ########## ########## ########## ##########

# a = [1, 2]
# b = [3, 4]
# tup = (a, b)

# a.append(1)

# print(tup)

########## ########## ########## ########## ##########

# a = [[1, 2, 3]]
# b = a[:]

# print(a, b)

########## ########## ########## ########## ##########

a = [[1, 2, 3]]
b = a[:]

a.append(1)

c = a[0]
c.append(4)

print(a is b)
print(a, b)