x = 1.0
y = 2

result = x + y
print(result)

##### ##### ##### ##### #####

x = -1
y = -2.0

result = x - y
print(result)

##### ##### ##### ##### #####

x = -1
y = -2.0

result = 4 - (-8)
print(result)

##### ##### ##### ##### #####

x = -1
y = -2.0

result = 4 * (-8)
print(result)

##### ##### ##### ##### #####

x = -1
y = -2.0

result = x * y
print(result)

##### ##### ##### ##### #####

x = 10
y = 2

result = x / y
print(result)

##### ##### ##### ##### #####

x = 10
y = 2.5

result = x / y  # regular division; results in a float along with its remainder, if any
print(result)

##### ##### ##### ##### #####

# x = 10
# y = 0

# result = x / y
# print(result)

x = 10
y = 2

result = x ** y  # exponential
print(result)

##### ##### ##### ##### #####

x = 10
y = 0

result = x ** y
print(result)

##### ##### ##### ##### #####

x = 10
y = -1

result = x ** y
print(result)

##### ##### ##### ##### #####

x = 11
y = 3

result = x // y  # integer division; converting whatever the float is to an integer without its remainder, if any
print(result)

##### ##### ##### ##### #####

x = 11
y = 2

result = x % y  # modulus division; gives you the remainder after division
print(result)

##### ##### ##### ##### #####

x = 11
y = 2
z = 4

# result = x % y / 4 * 7 ** 2 / 3
result = (x + y - z) ** (x % z)
# result = 9 ** 3
print(result)  # 729

##### ##### ##### ##### #####

result = (y % z) * 2 / 4
# result = 2 * 2 / 4
print(result)  # 1.0

##### ##### ##### ##### #####

result = (5 + x - z) ** y - 7 / 2 // 4
# result = 12 ** y - 7 / 2 // 4
# result = 144 - 7 / 2 // 4
# result = 144 - 3.5 // 4
# result = 144 - 0.0
print(result)  # 144.0

##### ##### ##### ##### #####

print(3.5 // 4)
#####  operator precedence #####
# [ 1st ] brackets / parenthesis
# [ 2nd ] exponents
# [ 3rd ] multiplication and division and modulus
# [ 4th ] addition subtraction

# if operators of the same precedence are present, we're going to execute them in the 
# order in which they occur / whatever comes first in the expression; left to right
# whatever comes to the left first and then whatever is on the right last

answer = "5" + "4"
print(answer)  # 54

##### ##### ##### ##### #####

answer = 4.5 / True
print(answer)  # 4.5

# answer = 4.5 / False
# print(answer)  # ZeroDivisionError