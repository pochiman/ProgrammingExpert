x = 2
y = 4

# True and True  # True
# True and False  # False
# False and True  # False 

compound = x < y and y + 2 > 3
# compound = True and True  # True
print(compound)

compound = x < y and False  # False
print(compound)

# True or True  # True
# True or False  # True
# False or True  # True
# False or False  $ False 

compound = x > y or y + 2 > 3  # True
print(compound)

# The NOT operator negates or swaps whatever the value of a condition is.
# It will evaluate this condition, and then whatever it's equal to, the NOT operator will give us the opposite.
# If this condition is true, NOT true is gonna be false.
# If this condition is false, NOT false is gonna be true.

compound = not (x < y)  # X is less than Y, so this is true. So the NOT of true is false, so it reverses the condition.
# compound = not (2 < 4)
# compound = not (True)  # False
print(compound)

compound = not (x < y and 1 == 1)  # False. Whatever's inside of here, it will simply swap it. 
print(compound)                    # It took this entire condition and then swapped it.

compound = not True == False
# compound = False == False  # True
print(compound)

compound = not (True == False)
# compound = False == False  # True
print(compound)

compound = True == not False  # SyntaxError # The NOT keyword has a lower precedence than the double equal sign.
print(compound)
# We try to evaluate this double equal sign before we try to evaluate NOT.
# What happens here is we actually try to say, true is equal to NOT false before we evaluate the NOT false.

# That means we're getting invalid syntax here because NOT false is evaluated after the double equals and 
# Python doesn't know how to interpret NOT false when it's looking at the double equal sign first.

# What's occurring is this is being evaluated first, and so this NOT false hasn't yet been changed to true 
# and Python doesn't yet know what to do with it.

# To fix this, you need to surround this in parentheses. So now if I put this in parentheses, it knows that 
# this should be done first and then we'll do the double equal sign.

compound = True == (not False)  # True
print(compound)

# It's precedence is lower than all of the comparison operators. 
compound = not True == False
# True == False  # False
# not False  # True
print(compound)
# So we get false and then we do the NOT.

# That's why it's valid on this side, because we do the comparison first 
# and then whatever the comparison is, we simply swap it.

# So we're not actually changing the NOT true to be equal to false and then comparing that.
# We're doing the condition first, and then we're swapping whatever the condition is to the reverse.
# So if it's false to true, if true to false.

# In most other languages, your NOT is gonna be an exclamation point.
# Your AND is gonna be two ampersands and your OR is gonna be two pipes like this. 
# They work the exact same way as the NOT, AND, and OR keywords, except they're just different symbols. 
# ! not
# && and
# || or

# How we combine AND, OR, and NOT, and how expressions are evaluated when we use all of these keywords together.
compound = True or False and not True or False  # do the NOT first
# compound = True or False and False or False   # do the AND next
# compound = True or False or False             # do the OR from left to right
# compound = True or False
# compound = True
print(compound)

# order of precedence
# [ 1st ] Conditional/Comparison operators 
# [ 2nd ] Not
# [ 3rd ] And
# [ 4th ] Or

compound = not (True or False) and not False or 2 < 3 or True  # parentheses first
# compound = not (True) and not False or 2 < 3 or True
# compound = not (True) and not False or True or True
# compound = False and not False or True or True
# compound = False and True or True or True
# compound = False or True or True
# compound = True or True
# compound = True
print(compound)

# De Morgan's Law which comes from Boolean algebra and it involves simplifying Boolean expressions.

# De Morgan's Law allows you to take a NOT that's being applied to a parenthesized expression and 
# apply it inside of the parentheses.

# Now the reason you want do this is because it allows you to more easily see what value of the 
# variables you need to make a condition true, or to make a condition false. 

# You have to imagine that X and Y are variables. That means we do not know what their value is. 
# Now we know they're gonna be true or false, but in a lot of cases, you're given an expression 
# and you're asked to find the value of X and Y that makes the expression true.

# So to do that, you can use De Morgan's Law to simplify.

# Now, De Morgan's Law also states the following, NOT (X OR Y) is equal to (NOT X) AND (NOT Y).
# So the way that De Morgan's Law works is when you have a NOT, you want to apply it to a 
# parenthesized expression, you have to swap whatever is in-between.

# So if it's an AND you swap it to an OR, if it's an OR you swap it to an AND, and then you have 
# to apply the NOT directly to the left-hand side and to the right-hand side of the expression.

# De Morgan's Law
# not (x and y) == (not x) or (not y)
# not (x or y) == (not x) and (not y)

# We need to get inside of here in the following format, (X AND Y) OR (X OR Y) so that we can apply the NOT to it.
# So when we look at our order of operations, we know that we need to do the AND first. 
not (w and z or (not w))

# So what I'm gonna do is surround my AND with parentheses.
# Now I am actually in the format X or Y where W and Z is my X, my left-hand side, and NOT W is my Y my right-hand side. 
# So I'm looking at the OR, what's the left of it is this, what's the right of it is this.
not ((w and z) or (not w))

# What I can do is take my NOT, apply it to this, swap this to an AND, and then take my NOT and apply it to this.
(not (w and z)) and (not (not w))

# Whenever you have two NOTs, they cancel out.
# So I'm looking at the left-hand side and I see I have a (not (W and Z)).
# This is in the format X and Y, so I can go and apply my NOT to the left and right-hand side and swap the sign. 
((not w) or (not z)) and w

# This now allows us very easily to figure out what values of W and Z will lead to this condition being true or false.
(not w) or (not z) and w

# Conditional/Comparison operators
# Not
# And
# Or

# Truth tables are the super simple way to figure out what values you need in a condition or in a boolean expression 
# in this case to make this true. 

# So we have our variables W and Z, but I want to know what value of W and what value of Z or what values, because 
# there is sometimes multiple answers here that will make this condition true. This involves making a truth table.

# [ 1 ] You create one column for each variable that you have. So we have our variables W and Z.
# [ 2 ] Figure out every single possible combination of true and false for W and Z.
# [ 3 ] You go false, true, false, true. You alternate every other time. You can also go in the other order.
# [ 4 ] Then in the second column, you're gonna alternate every two falses, so now I go false, false, true, and true.
# [ 5 ] And Now I've generated every single possible combination of true and false for W and Z.

'''
W Z
---
F F -> True
T F -> True
F T -> True
T T -> False
'''

# [ 6 ] If I added another variable, let's just add, say Y here, and let's continue this.
# [ 7 ] Since I added another variable, I'm now gonna have four more possible combinations. 
# [ 8 ] So we need to continue these columns.
# So every time you add another variable, you have two more options for this variable.

# And so what ends up happening is you have the number of options, which is equal to two, 
# to the exponent of how many variables you have. 

# So that's how many different combinations of true and false you're gonna have for all of these variables.
# You have two, to whatever the number of variables is.
# So previously, we only had two variables, and so we add to the two that gave us four combinations. 

# However, now that we have three, we have eight total combinations. 
# And that's how you generate the combinations. In the first column, you have false, true, alternate every one, 
# then alternate every two, then alternate every four, then every eight, then every 16, then every 32, it's just 
# basically using the exponents. 

'''
W Z Y
-----
F F F
T F F
F T F
T T F

F F T
T F T
F T T
T T T
'''

# So anyways, this is our truth table; I only want to have the two columns.
'''
W Z
---
F F
T F
F T
T T
'''

# I simply plug in these values into this expression and see if it gives me true or false.
# Let's look at false and false. 

# (not W), W is false, so that's gonna give me true.
# OR, and then we have (not Z), Z is false, so that is true. 
# and then we have (and W). 
# Now we have (and W), well AND is false. 
# So we have true OR true AND false. 
(not w) or (not z) and w

# First we do true AND false.
True or (True and False)
# We see that true AND false is gonna give us false.
True or False
# And then we have true OR false, that's gonna give us true.
True

'''
W Z
---
F F -> True
'''



(not w) or (not z) and w
False or (True and True)
False or True
True

'''
W Z
---
T F -> True
'''



(not w) or (not z) and w
True or (False and False)
True or False
True

'''
W Z
---
F T -> True
'''



(not w) or (not z) and w
False or (False and True)
False or False
False

'''
W Z
---
T T -> False
'''

# Remember that you need to get your interior expression into this format.
not ((w and z) or (not w))

# So the way you do that is by adding parentheses in the proper places, you're 
# going to apply your ANDs first, then your OR second. 

# Just to show you a quick example, if we had another OR in our expression. 
# You can separate this however you want because the ORs have the same precedence level.
not (w or z or (not w))

# And both of these are completely valid, you've now turned this into the correct format 
# to use De Morgan's Law and of course the same applies for AND.
not ((w or z) or (not w))
not (w or (z or (not w)))