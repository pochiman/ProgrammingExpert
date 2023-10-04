for i in range(20):  # stop
    print(i)  # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

########## ########## ########## ########## ##########

for i in range(5, 20):  # start, stop
    print(i)  # 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

########## ########## ########## ########## ##########

for i in range(5, 20, 2):  # start, stop, step
    print(i)  # 5 7 9 11 13 15 17 19

########## ########## ########## ########## ##########

for i in range(5, 19, 2):
    print(i)  # 5 7 9 11 13 15 17

########## ########## ########## ########## ##########

for i in range(0, 20, 5):
    print(i)  # 0 5 10 15

########## ########## ########## ########## ##########

for i in range(-5, -20, -5):
    print(i)  # -5 -10 -15

########## ########## ########## ########## ##########

for i in range(10, -20, -5):
  print(i)  # 10 5 0 -5 -10 -15

########## ########## ########## ########## ##########

result = 0

for i in range(1, 11):
  result += i

print(result)  # 55

########## ########## ########## ########## ##########

lst = [1, 2, 3, 4, 5, True, False]

for i in range(7):  # iterating through all six indices in lst
  print(lst[i])  # 1 2 3 4 5 True False

########## ########## ########## ########## ##########

lst = [1, 2, 3, 4, 5, True]

for idx in range(len(lst)):  # iterating by the index
  print(lst[idx])  # 1 2 3 4 5 True

for element in lst:  # iterating by item
    print(element)  # 1 2 3 4 5 True

for i, element in enumerate(lst):  # iterating by both the index and the element
    print(i, element)

# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
# 5 True

########## ########## ########## ########## ##########

tup = (2, 3, 4, "hello", "tim", True)

for i in range(len(tup)):
    element = tup[i]
    print(element)  # 2 3 4 hello tim True

for element in tup:
    print(element)  # 2 3 4 hello tim True

for i, element in enumerate(tup):
    print(i, element)

# 0 2
# 1 3
# 2 4
# 3 hello
# 4 tim 
# 5 True

########## ########## ########## ########## ##########

s = "my string"

for i in range(len(s)):
    print(s[i])

# m
# y

# s
# t
# r
# i
# n
# g

s = "my string"

for i in range(5):
    print(s[i])

# m
# y

# s
# t

s = "my string"

for i in range(0, len(s), 2):
    print(s[i])

# m

# t
# i
# g

########## ########## ########## ########## ##########

lst = [1, 2, 3, 3, 4, 4, 2, 1, 2]

for num in lst:
    if num == 4:
        break

    print(num)

print("Done")

# 1
# 2
# 3
# 3
# Done

########## ########## ########## ########## ##########

lst = [1, 2, 3, 3, 4, 4, 2, 1, 2]

for num in lst:
    if num == 4:
        continue

    print(num)

print("Done")

# 1
# 2
# 3
# 3
# 2
# 1
# 2
# Done

########## ########## ########## ########## ##########

for i in range(10):
    for j in range(10):
        print(i, j)

# 0 0
# 0 1
# 0 2
# 0 3
# 0 4
# 0 5
# 0 6
# 0 7
# 0 8
# 0 9
# ...

for i in range(10):
    for j in range(10):
        for w in range(2):
            print(i, j, w)

# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 0 2 0
# 0 2 1
# 0 3 0
# 0 3 1
# 0 4 0
# 0 4 1
# 0 5 0
# 0 5 1
# 0 6 0
# 0 6 1
# 0 7 0
# 0 7 1
# 0 8 0
# 0 8 1
# 0 9 0
# 0 9 1
# .....

########## ########## ########## ########## ##########

lst = [[1, 2], [3, 4], [5, 6], [7, 8]]

for i in range(len(lst)):
    interior_lst = lst[i]

    for j in range(len(interior_lst)):
        print(interior_lst[j])  # 1 2 3 4 5 6 7 8

########## ########## ########## ########## ##########

string = "hello world!"

for i, char in enumerate(string):
  if char == "w":
    print(i)  # 6

########## ########## ########## ########## ##########

numbers = []  # This needs to be declared outside of the for loop so we are not constantly 
              # redefining it inside and it's actually gonna store all of our numbers.  
for i in range(3):
    num = input("Enter a number: ")
    numbers.append(int(num))

print(numbers)

# Enter a number: 2
# Enter a number: 4
# Enter a number: 5
# [2, 4, 5]

########## ########## ########## ########## ##########

for i in range(3):
    pass  # It acts as a placeholder. What it does is just sit there and do nothing.

########## ########## ########## ########## ##########

words = ("hello", "name", "this", "is", "word")
target = "name"

found = False  # a boolean

for word in words:
    if word == target:
        print("I found the word!")
        found = True

if not found:  # If it is False, then this will evaluate to True and I will print this.
    print("I didn't find the word!")  # I found the word!

########## ########## ########## ########## ##########

words = ("hello", "name", "this", "is", "word")
target = "name"

for word in words:
    if word == target:
        print("I found the word!")  # I found the word!
        break
else:
    print("I didn't find the word!")