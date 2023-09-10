# Which expression is equivalent to the following expression?
not(x and not (y and z))

# Answer
(not x) or (y and z)

##### Explanation #####
# De Morgan's laws state that not (x and y) == not x or not y and not (x or y) == not x and not y.
# Applying these laws, you can simplify the condition one step at a time:

# Step by step:
[ 1 ] not(x and not (y and z))
[ 2 ] = (not x) or (not (not (y and z)))
[ 3 ] = (not x) or (y and z)