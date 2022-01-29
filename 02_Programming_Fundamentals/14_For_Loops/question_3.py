# Use a single for loop to print the numbers in the range of 1 to 10, inclusive, each on a separate line.

##### Expected Output #####
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

##### Solution 1 #####
# for idx in range(1, 11):
#     print(idx)

##### Solution 2 #####
# for idx in range(10):
#     print(idx + 1)

##### Solution 3 #####
num = 1
for idx in range(10):
    print(num)

    num += 1