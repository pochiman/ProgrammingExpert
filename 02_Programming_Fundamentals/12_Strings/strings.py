s = "hello"

print(s[0])    # h
print(s[-1])   # o
print(len(s))  # 5
count = s.count("l")  # 2
print(count)

########## ########## ########## ########## ##########

index = s.find("l")  # 2
print(index)

########## ########## ########## ########## ##########

index = s.find("a")  # -1 # If the character does not exist, rather than an error, it's going to return negative one.
# .find does not work on lists, it only works on strings.
print(index)

########## ########## ########## ########## ##########

upper = s.upper()  # HELLO
print(upper)

########## ########## ########## ########## ##########

s = "hELlo"

lower = s.lower()  # hello
print(lower)

########## ########## ########## ########## ##########

answer = input("What is my name? ")

if answer.lower() == "tim":
    print('Correct')
else:
    print("Incorrect")

########## ########## ########## ########## ##########

s = "algoexpert"

print(s.capitalize())  # Algoexpert

########## ########## ########## ########## ##########

s = "algoexpert"

contains = "h" in s  # False
print(contains)

contains = "a" in s  # True
print(contains)

########## ########## ########## ########## ##########

s = "19"

is_digit = s.isdigit()  # True # This method checks if this string is a digit.

print(is_digit)



s = "19h"

is_digit = s.isdigit()  # False # The string does not represent a valid integer.

print(is_digit)



s = "19.4"

is_digit = s.isdigit()  # False # All isdigit is telling me is if this is actually an int, not if it is a float.

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

words = s.split()  # ['hello', 'my', 'name', 'is', 'tim']

print(words)



s = "hello,my,name,is,tim"

words = s.split()  # ['hello,my,name,is,tim']  # Because there was no spaces, and so this wasn't able to split it.

print(words)



s = "hello,my,name,is,tim"

words = s.split(",")  # ['hello', 'my', 'name', 'is', 'tim']  # Now it's going to split by the commas.
# So now, we get all of the individual words, and all of the commas were removed.
# (",") is called your delimiter or separator. This will be removed from the string that you are 
# splitting and it will give you all of the words that are in between all of these little symbols.
print(words)

########## ########## ########## ########## ##########

s = "hello,my,name,is,,,tim"

s2 = s.replace(",", "|")  # hello|my|name|is|||tim

print(s2)

########## ########## ########## ########## ##########

name = input("Name: ")

s = f"Hello, {name}! Thanks!"  # Hello, Tim! Thanks!

print(s)

########## ########## ########## ########## ##########

name = input("Name: ")

print(f"Hello, {name}! Thanks! {1 + 4}, {name}")  # Hello, Tim! Thanks! 5, Tim

########## ########## ########## ########## ##########

name = input("Name: ")

print(name * 5)  # TimTimTimTimTim

########## ########## ########## ########## ##########

name = input("Name: ")

string = """hello my name is tim
and this is a multiline string
!
"""
print(string)

########## ########## ########## ########## ##########

name = input("Name: ")

string = f'{name}\'s'  # escaping a character

print(string)  # Tim's

########## ########## ########## ########## ##########

lst = ["t", "i", "m"]
string = "-".join(lst)  # t-i-m

print(string)