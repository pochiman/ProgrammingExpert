# "4" -> int -> float
# 45 -> str -> float

x = "4"
y = int(x) + 4
print(type(y))
print(type(x))
print(y)

##### ##### ##### ##### #####

y = int("4") + 4
print(y)

##### ##### ##### ##### #####

y = float("4.5") + 4
print(y)

##### ##### ##### ##### #####

y = float("4") + 4
print(y)

##### ##### ##### ##### #####

y = int(True)  # evaluates to 1
print(y)

##### ##### ##### ##### #####

y = int(False)  # evaluates to 0
print(y)

##### ##### ##### ##### #####

y = int(4.7)  # removes any of the decimal aspect of this float
print(y)

# y = int("4.7")  # it is no longer going to work because we cannot convert the string 4.7 to an int
# print(y)

y = bool("0")  # if the string has any content in it, any characters in it whatsoever, this is actually going to be True
print(y)

##### ##### ##### ##### #####

y = bool(" ")  # even a space we are going to get True
print(y)

##### ##### ##### ##### #####

y = bool("")  # if I have an empty string and I try to convert this to a boolean, I get False
print(y)

##### ##### ##### ##### #####

y = bool(-9)  # any number is going to evaluate to True except for the number 0
print(y)

##### ##### ##### ##### #####

y = bool(0)  # zero will evaluate to False because zero represents False
print(y)

##### ##### ##### ##### #####

y = str(0) + "0"
print(y)

##### ##### ##### ##### #####

y = str(1) + "0"
print(y)

##### ##### ##### ##### #####

number = input("Enter a number: ")
result = int(number) + 5
print("The result is:", result)

##### ##### ##### ##### #####

number = input("Enter a number: ")
result = float(number) + 5
print("The result is:", result)