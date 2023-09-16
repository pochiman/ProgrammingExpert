x = (1, 2, 3)
print(x[-1])  # 3

# x[0] = 2  # TypeError # I cannot directly modify the elements inside of it.

# Tuple: immutable object / cannot be modified
# List: mutable object / can be modified

# tuple()  # Just like list, we can use the tuple function to create a tuple.

x = (1, 2, 3, (1, 2), True, [])
print(x[-1])  # []

print(len(x)) # 6

count = x.count(1)
print(count)  # 2

index = x.index(1)
print(index)  # 0 
# This will give us the index of the first occurrence of whatever element we're looking for.

contains = 2 in x
print(contains)  # True

print(x)  # (1, 2, 3, (1, 2), True, [])

print(x[3])  # (1, 2)

print(x[3][0])  # 1

########## ########## ########## ########## ##########

x = (1, 2)
y = (3, 4)

combined = x + y
print(combined)  # (1, 2, 3, 4)

combined = x * 2
print(combined)  # (1, 2, 1, 2)

combined = [1, 2] * 2  
# We can also do this with lists.
print(combined)  # [1, 2, 1, 2]

combined = [1] * 10
print(combined)  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

########## ########## ########## ########## ##########

x = 1, 2, 3, 4  
# If I start defining a bunch of elements separated by commas, this will automatically make this a tuple.
print(x)  # (1, 2, 3, 4)

x = 1, 2
# This is a valid tuple.
print(x)  # (1, 2)

x = (1)
# This is not a tuple. Whenever you only have one element inside of a tuple 
# or parentheses, by default, it's just going to evaluate this as an int.
print(x)  # 1

########## ########## ########## ########## ##########

x = (1, )
# If you actually want a one element tuple, you need to do one 
# comma and then just don't put anything for the second element.
# And now this will actually be read as a one element tuple.
print(x)     # 1
print(x[0])  # 1

########## ########## ########## ########## ##########

# If we wanted to actually modify a tuple, we would need 
# to create a brand new tuple and then change the element.

# So I'm just grabbing the first element from x, the last 
# element from x, and then I'm changing the middle element.
x = (1, 2, 3)
y = (x[0], 4, x[2])
print(y)  # (1, 4, 3)