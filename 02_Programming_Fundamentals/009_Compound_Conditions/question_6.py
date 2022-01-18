# Set the values of w, x, y, and z such that all of the condition_ variables evaluate to True.
# Only use boolean values.

# w = None  # <- Change this
# x = None  # <- Change this
# y = None  # <- Change this
# z = None  # <- Change this

w = True
x = True
y = False
z = True

# Don't change any of these `condition_` variables.
condition_1 = w and x and not y or not z
# w = True and x = True and y = False or z = True
condition_2 = not (w and not w)
# True
condition_3 = not (w and y or y)
# True
condition_4 = x and (y or z and w)
# True and (False or True and True)

# All of these should print `True`.
print(condition_1)
print(condition_2)
print(condition_3)
print(condition_4)