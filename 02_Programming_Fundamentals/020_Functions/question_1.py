# Write a function named add that takes in two parameters x and y, both expected
# to be numbers.  Your function should add the two numbers and return the result.

##### Solution 1 #####
# def add(x, y):
#     return x + y

##### Solution 2 #####
def add(x, y):
    try:
        return x + y
    except Exception as e:
        # It can be a good practice to handle potential exceptions!
        print("Something went wrong; make sure to pass numbers to this function!")