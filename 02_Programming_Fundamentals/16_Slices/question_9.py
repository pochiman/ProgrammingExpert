# Modify the w, x, y, and z variables such that the program outputs [8, 6, 4].

##### Expected Output #####
# [8, 6, 4]

# w = None  # <- Change this
# x = None  # <- Change this
# y = None  # <- Change this
# z = None  # <- Change this

w = 2
x = 2
y = -3
z = -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_slice = lst[::z] # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
second_slice = first_slice[:y] # [10, 9, 8, 7, 6, 5, 4] 
third_slice = second_slice[x:] # [8, 7, 6, 5, 4]
last_slice = third_slice[::w] # [8, 6, 4]

print(last_slice)
# [8, 6, 4]