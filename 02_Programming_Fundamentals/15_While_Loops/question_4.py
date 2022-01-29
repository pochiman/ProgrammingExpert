# Use a while loop to print the squares of the numbers: 1, 3, 6, 10, 15 and 21.

##### Expected Output #####
# 1
# 9
# 36
# 100
# 225
# 441

##### Solution 1 #####

# nums = [1, 3, 6, 10, 15, 21]
# idx = 0

# while idx < len(nums):
#     num = nums[idx]
#     print(num * num)

#     idx += 1

##### Solution 2 #####

num = 1
step = 2

while num <= 21:
    print(num * num)

    num += step
    step += 1    