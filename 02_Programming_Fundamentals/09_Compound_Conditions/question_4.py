# What is the precedence of the logical operators in Python? 
# In other words, in what order are the logical operators evaluated?

# Answer
not, and, then or

##### Explanation #####
# In Python, the precedence of the logical operators is not, and, then or.

# This means that the compound condition True and not False or not True 
# would be evaluated as (True and (not False)) or (not True).