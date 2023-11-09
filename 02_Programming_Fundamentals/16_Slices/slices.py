my_list = [2, 3, 4, 2, 3, 1, 2]
my_list = [2, 3, 4, 2, 3, 1, 2, 2, 3, 1, 2, 1]
new_list = my_list[0:2]
new_list = my_list[:4]
new_list = my_list[1:4]
new_list = my_list[1:6:2]
new_list = my_list[:8:3]
new_list = my_list[8:0:-1]
new_list = my_list[-4:0:-1]
new_list = my_list[:]
new_list = my_list[::2]
new_list = my_list[::-1]
print(new_list)

########## ########## ########## ########## ##########

string = "hello world"

print(string[::2])
print(string[1::2])
print(string[1:6:2])

########## ########## ########## ########## ##########

tup = 1, 2, 3, 4, 2, 3

print(tup[1:6:2])
print(tup[::-1])