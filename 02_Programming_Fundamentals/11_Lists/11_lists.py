# x = [1, 2, 3, True, 3.4, "Hello"]
# # print(x[0])
# x.append("last element")
# x.append(2)
# print(len(x))
# print(len("str"))

# s = "hello"

# print(s[0])

########## ########## ########## ########## ##########

# x = [1, 2, 3, True, 3.4, "Hello"]

# popped = x.pop()

# print(popped)
# print(x)

########## ########## ########## ########## ##########

# x = [1, 2, 3, 1, 1, 1, 1, 3.4, "Hello"]

# count = x.count(1)
# index = x.index(3)
# x.remove(1)

# print(index)
# print(x)

########## ########## ########## ########## ##########

# x = [1, 2, 3, 1, 1, 1, 1, 3.4, 5, "Hello"]

# list_contains_5 = 5 in x
# list_contains_5 = x.count(5) > 0

# print(list_contains_5)

########## ########## ########## ########## ##########

# x = [1, 2, 3, 1, 1, 1, 1, 3.4, "Hello"]

# print(x[-1])
# print(x[-9])

########## ########## ########## ########## ##########

# x = [1, 2, 3]
# y = [1, 2]

# combined = x + y
# combined[0] = 100
# print(combined)
# print(x)
# print(y)

########## ########## ########## ########## ##########

# x = [1, 2, 3]
# y = [1, 2]

# x.extend([1, 2])
# x.extend(y)
# y.extend(x)

# print(x)
# print(y)

########## ########## ########## ########## ##########

lst = [[5, 6, [100]], [2, 3], [1, 2, 3]]
print(lst[-1][1])
print(lst[0][2])
print(lst[0][2][0])