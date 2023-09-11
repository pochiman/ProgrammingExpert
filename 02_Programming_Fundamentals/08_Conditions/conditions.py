cond = 2 == 3  # False
print(cond)

##### ##### ##### ##### #####

cond = 3 == 3  # True
print(cond)

##### ##### ##### ##### #####

cond = 3.0 == 3  # True
print(cond)

##### ##### ##### ##### #####

cond = 3.0 != 3  # False
print(cond)

##### ##### ##### ##### #####

cond = 3.1 != 3  # True
print(cond)

##### ##### ##### ##### #####

x = 4
y = 4

cond = x != y  # False

print(cond)

##### ##### ##### ##### #####

cond = x != 9  # True

print(cond)

##### ##### ##### ##### #####

cond = x < 9  # True

print(cond)

##### ##### ##### ##### #####

x = 9
y = 4

cond = x < 9  # False

print(cond)

##### ##### ##### ##### #####

cond = x < 9.5  # True

print(cond)

##### ##### ##### ##### #####

cond = x > 9.5  # False

print(cond)

##### ##### ##### ##### #####

cond = x + 2 > 9.5  # True

print(cond)

##### ##### ##### ##### #####

cond = x + 2 > 9.5 + 1  # True

print(cond)

##### ##### ##### ##### #####

cond = x <= 9  # True

print(cond)

##### ##### ##### ##### #####

cond = x >= 9  # False

print(cond)

# cond = x >= "6"  # TypeError

# print(cond)

cond = x == "6"  # False

print(cond)

##### ##### ##### ##### #####

cond = x != "6"  # True

print(cond)

# cond = x < "6"  # TypeError

# print(cond)

str1 = "hello"
str2 = "Hello"

cond = str1 == str2  # False

print(cond)

##### ##### ##### ##### #####

cond = str1 != str2  # True

print(cond)

##### ##### ##### ##### #####

str1 = "hello"
str2 = "hello "

cond = str1 == str2  # False

print(cond)

##### ##### ##### ##### #####

str1 = "hello"
str2 = "hello"

cond = str1 < str2  # False

print(cond)

##### ##### ##### ##### #####

str1 = "a"
str2 = "b"

cond = str1 < str2  # True

print(cond)

##### ##### ##### ##### #####

str1 = "a"
str2 = "B"

cond = str1 < str2  # False

print(cond)

# The way that we actually compare strings is by using what's known as their ASCII value. 

str1 = "ac"
str2 = "ab"

cond = str1 <= str2  # False; c is greater than b and so that means this condition will be False

print(cond)

# Every single character on your keyboard has a numeric value associated with it.

print(ord("a"))
print(ord("A"))
print(ord("!"))
# ASCII #
# "a" - 97
# "A" - 65
# "B" - 66

# In Python, there are these two functions:
# ord()  # ordinal
# chr()  # character

# The ordinal function gives you the numeric representation of any character that you pass to it.
print(ord("a"))  # 97 is the ASCII value of "a"
print(ord("A"))  # 65 is the ASCII value of "A"
print(ord("!"))  # 33 is the ASCII value of "!"
# When you're comparing an upper case to a lower case, the upper case will always be less than the lower case.

# The char function takes an ordinal value and gives you the character associated with it.
print(chr(76))  # L is the character associated with the ordinal value 76.
print(chr(98))  # b is the character associated with the ordinal value 98.

str1 = "ABc"
str2 = "aBC"

cond = str1 <= str2  # True because "A" is 65 and "a" is 97. string 1 is gonna be less than string 2.

print(cond)

##### ##### ##### ##### #####

str1 = "ABc"
str2 = "ABC"

cond = str1 <= str2  # False because lowercase "c" is greater than uppercase "C"

print(cond)

##### ##### ##### ##### #####

str1 = "ABc"
str2 = "ABC"

cond = str1 > str2  # True

print(cond)

##### ##### ##### ##### #####

cond = True == 1  # True because True really is one. 

# When it comes to math and doing comparisons, we can assume that True is equal to one.
# In the same way, we can assume that False is equal to zero.

print(cond)

##### ##### ##### ##### #####

cond = False == 0  # True

print(cond)

##### ##### ##### ##### #####

cond = False == ""  # False

print(cond)

##### ##### ##### ##### #####

cond = True == ""  # False

print(cond)

##### ##### ##### ##### #####

cond = True == "True"  # False because they are different types.

print(cond)