##### Range Generator #####

# Write a generator named new_range that is initialized by passing three integer values, a start, stop and step.
# Your generator should mimic the range function in functionality but always accept three integer values.

# You may assume all three of these initialization values will always be integers and that the step will never be zero.

##### Sample Output #####
# >>> r = new_range(2, 5, 1)
# >>> for x in r:
#         print(x)
# 2
# 3
# 4
# >>> r = new_range(-2, -5, -1)
# >>> for x in r:
#         print(x)
# -2
# -3
# -4

##### Solution 1 #####
# def new_range(start, stop, step):
#     current = start

#     while True:
#         if step < 0 and current <= stop:
#             break
#         if step > 0 and current >= stop:
#             break

#         yield current
#         current += step

##### Solution 2 #####
def new_range(start, stop, step):
    for i in range(start, stop, step):
        yield i