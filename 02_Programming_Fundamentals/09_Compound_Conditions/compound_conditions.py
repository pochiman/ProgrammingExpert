x = 2
y = 4

compound = x < y and y + 2 > 3
print(compound)

compound = x < y and False
print(compound)

compound = not (x < y and 1 == 1)
print(compound)

compound = not True == False
print(compound)

compound = True == (not False)
print(compound)

# ! not
# && and
# || or

compound = True or False and not True or False
print(compound)

# Conditional/Comparison operators
# Not
# And
# Or

compound = not (True or False) and not False or 2 < 3 or True
print(compound)

# DeMorgan's Law
# not (x and y) == (not x) or (not y)
# not (x or y) == (not x) and (not y)

not ((w and z) or (not w))

(not (w and z)) and (not (not w))

(not w) or (not z) and w

'''
W Z
---
F F -> True  # True or (True and False)
T F -> True  # False or (True and True)
F T -> True  # True or False and False
T T -> False # False or False and True
'''