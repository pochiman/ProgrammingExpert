# for i in range(20):
#   print(i)

########## ########## ########## ########## ##########

# for i in range(5, 20):
#   print(i)

########## ########## ########## ########## ##########

# for i in range(5, 20, 2):
#   print(i)

########## ########## ########## ########## ##########

# for i in range(5, 19, 2):
#   print(i)

########## ########## ########## ########## ##########

# for i in range(0, 20, 5):
#   print(i)

########## ########## ########## ########## ##########

# for i in range(-5, -20, -5):
#   print(i)

########## ########## ########## ########## ##########

# for i in range(10, -20, -5):
#   print(i)

########## ########## ########## ########## ##########

# result = 0

# for i in range(1, 11):
#   result += i

# print(result)

########## ########## ########## ########## ##########

# lst = [1, 2, 3, 4, 5, True, False]

# for i in range(7):
#   print(lst[i])

########## ########## ########## ########## ##########

# lst = [1, 2, 3, 4, 5, True]

# for i in range(len(lst)):
#   print(lst[i])

# for element in lst:
#   print(element)

# for i, element in enumerate(lst):
#   print(i, element)

########## ########## ########## ########## ##########

# tup = (2, 3, 4, "hello", "tim", True)

# for i in range(len(tup)):
#   element = tup[i]
#   print(element)

# for element in tup:
#   print(element)

# for i, element in enumerate(tup):
#   print(i, element)

########## ########## ########## ########## ##########

# s = "my string"

# for i in range(len(s)):
#   print(s[i])

# for i in range(5):
#   print(s[i])

# for i in range(0, len(s), 2):
#   print(s[i])

########## ########## ########## ########## ##########

# lst = [1, 2, 3, 3, 4, 4, 2, 1, 2]

# for num in lst:
#   if num == 4:
#     break

#   print(num)

# print("Done")

########## ########## ########## ########## ##########

# for num in lst:
#   if num == 4:
#     continue

#   print(num)

# print("Done")

########## ########## ########## ########## ##########

# for i in range(10):
#   for j in range(10):
#     for w in range(2):
#       print(i, j, w)

########## ########## ########## ########## ##########

# lst = [[1, 2], [3, 4], [5, 6], [7, 8]]

# for i in range(len(lst)):
#   interior_lst = lst[i]

#   for j in range(len(interior_lst)):
#     print(interior_lst[j])

########## ########## ########## ########## ##########

# st = "hello world!"

# for i, char in enumerate(st):
#   if char == "w":
#     print(i)

########## ########## ########## ########## ##########

# numbers = []

# for i in range(3):
#   num = input("Enter a number: ")
#   numbers.append(int(num))

# print(numbers)

########## ########## ########## ########## ##########

# for i in range(3):
#   pass

########## ########## ########## ########## ##########

# words = ("hello", "name", "this", "is", "word")
# target = "name"

# found = False

# for word in words:
#   if word == target:
#     print("I found the word!")
#     found = True

# if not found:
#   print("I didn't find the word!")

########## ########## ########## ########## ##########

words = ("hello", "name", "this", "is", "word")
target = "name"


for word in words:
  if word == target:
    print("I found the word!")
    break
else:
  print("I didn't find the word!")  