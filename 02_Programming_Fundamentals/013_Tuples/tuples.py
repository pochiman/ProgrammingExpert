x = (1, 2, 3, (1, 2), True, [])
print(x[-1])

print(len(x))

count = x.count(1)
print(count)

index = x.index(1)
print(index)

contains = 2 in x
print(contains)

print(x)

print(x[3][0])

########## ########## ########## ########## ##########

a = (1, 2)
b = (3, 4)

combined = a + b
print(combined)

combined = a * 2
print(combined)

combined = [1, 2] * 2
print(combined)

combined = [1] * 10
print(combined)

########## ########## ########## ########## ##########

x = 1, 2, 3, 4

print(x)

########## ########## ########## ########## ##########

x = (1, )

print(x[0])

########## ########## ########## ########## ##########

x = (1, 2, 3)
y = (x[0], 4, x[2])
print(y)