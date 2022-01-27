s = "hello"

print(s[0])
print(s[-1])
print(len(s))
count = s.count("l")
print(count)

########## ########## ########## ########## ##########

index = s.find("l")
print(index)

########## ########## ########## ########## ##########

index = s.find("a")
print(index)

########## ########## ########## ########## ##########

upper = s.upper()
print(upper)

########## ########## ########## ########## ##########

s = "hELlo"

lower = s.lower()
print(lower)

########## ########## ########## ########## ##########

answer = input("What is my name? ")

if answer.lower() == "tim":
  print('Correct')
else:
  print("Incorrect")

########## ########## ########## ########## ##########

s = "algoexpert"

print(s.capitalize())

########## ########## ########## ########## ##########

s = "algoexpert"

contains = "h" in s
print(contains)

contains = "a" in s
print(contains)

########## ########## ########## ########## ##########

s = "19"

is_digit = s.isdigit()

print(is_digit)

########## ########## ########## ########## ##########

num = input("Number: ")

if num.isdigit():
  print("It is a number")
  num = int(num)
  print(num + 5)
else:
  print('This is not an int')

########## ########## ########## ########## ##########

s = "hello my name is tim"

words = s.split()

print(words)

s = "hello,my,name,is,tim"

words = s.split(",")

print(words)

########## ########## ########## ########## ##########

s = "hello,my,name,is,,,tim"

s2 = s.replace(",", "|")

print(s2)

########## ########## ########## ########## ##########

name = input("Name: ")

# s = f"Hello, {name}! Thanks! {1 + 4}, {name}"

# print(s)

print(f"Hello, {name}! Thanks! {1 + 4}, {name}")

########## ########## ########## ########## ##########

name = input("Name: ")

print(name * 5)

########## ########## ########## ########## ##########

name = input("Name: ")

string = """hello my name is tim
and this is a multiline string
!
"""
print(string)

########## ########## ########## ########## ##########

name = input("Name: ")

string = f'{name}\'s'

print(string)

########## ########## ########## ########## ##########

lst = ["t", "i", "m"]
string = "-".join(lst)

print(string)