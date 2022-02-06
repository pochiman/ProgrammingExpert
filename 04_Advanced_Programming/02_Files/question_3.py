##### Writing To Files #####

# Within the current directory, create a new file named "programmingExpert.txt" 
# that contains the squares of numbers in the range 1 to 50, each on a new line.

##### Sample File Content #####
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# 121
# 144
# 169
# 196
# 225
# 256
# 289
# 324
# 361
# 400
# 441
# 484
# 529
# 576
# 625
# 676
# 729
# 784
# 841
# 900
# 961
# 1024
# 1089
# 1156
# 1225
# 1296
# 1369
# 1444
# 1521
# 1681
# 1764
# 1849
# 1936
# 2025
# 2116
# 2209
# 2304
# 2401
# 2500

##### Solution 1 #####
# with open("programmingExpert.txt", "w") as file:
#     for num in range(1, 51):
#         square = num ** 2
#         file.write(str(square) + "\n")

##### Solution 2 #####
file = open("programmingExpert.txt", "w")

for num in range(1, 51):
    square = num ** 2
    file.write(str(square) + "\n")

file.close()