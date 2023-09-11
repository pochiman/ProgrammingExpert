x = [1, 2, 3, True, 3.4, "Hello"]
print(x[0])
x.append("last element")
x.append(2)
print(len(x))
print(len("str"))

s = "hello"

print(s[0])

########## ########## ########## ########## ##########

x = [1, 2, 3, True, 3.4, "Hello"]

popped = x.pop()

print(popped)
print(x)

########## ########## ########## ########## ##########

x = [1, 2, 3, 1, 1, 1, 1, 3.4, "Hello"]

count = x.count(1)  # 5
index = x.index(1)  # 0 # This gives the index of the first one that occurs in my list, going from left to right.
index = x.index(3)  # 2
x.remove(1)         # This will remove the first occurrence of whatever element we pass here from the list.

print(index)
print(x)

########## ########## ########## ########## ##########

x = [1, 2, 3, 1, 1, 1, 1, 3.4, 5, "Hello"]

list_contains_5 = 5 in x  # in is a way you can check if an element exists inside of your list, yielding True or False.
list_contains_5 = x.count(5) > 0

print(list_contains_5)

########## ########## ########## ########## ##########

x = [1, 2, 3, 1, 1, 1, 1, 3.4, "Hello"]

print(x[-1])  # Hello
print(x[-9])  # 1

########## ########## ########## ########## ##########

x = [1, 2, 3]
y = [1, 2]

combined = x + y  # This will give me a brand new list that has all the elements in x, then all the elements in y.
print(combined)   # [1, 2, 3, 1, 2]

combined[0] = 100
print(combined)   # [100, 2, 3, 1, 2]
print(x)          # [1, 2, 3]  
print(y)          # [1, 2]  

########## ########## ########## ########## ##########

x = [1, 2, 3]
y = [1, 2]

x.extend([1, 2])  # [1, 2, 3, 1, 2]
x.extend(y)       # [1, 2, 3, 1, 2]
y.extend(x)       # [1, 2, 1, 2, 3, 1, 2]

print(x)
print(y)

########## ########## ########## ########## ##########

lst = [[5, 6, [100]], [2, 3], [1, 2, 3]]  # multidimensional list
print(lst[-1][1])    # 2
print(lst[0][2])     # [100]
print(lst[0][2][0])  # 100