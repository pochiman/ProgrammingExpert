x = 0
while x < 5:
    print(x)  # 0 1 2 3 4
    x += 1

##### OR #####

for x in range(5):
    print(x)

########## ########## ########## ########## ##########

num = input("Enter an integer: ")

while not num.isdigit():
    num = input("Enter an integer: ")

########## ########## ########## ########## ##########

while True:
    num = input("Enter an integer: ")
    if num.isdigit():
        break

########## ########## ########## ########## ##########

lst = [2, 3, 3, -2, -2, -1]

result = 0
i = 0

while result < 9 and i < len(lst):
    num = lst[i]
    result += num
    i += 1

    print(num)

########## ########## ########## ########## ##########

lst = [2, 3, 3, -2, -2, -1]
i = 0

while i < len(lst):
    if lst[i] == -2:
        print("found it")
        break
    i += 1
else:
    print("didn't find it")