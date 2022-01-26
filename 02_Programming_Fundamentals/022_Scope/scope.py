# x = 1

# def foo():
  # x = 0
#   print(x)

# foo()
# print(x)

########## ########## ########## ########## ##########

# inp = int(input("Enter a number: "))

# if inp > 5:
#   value = "Greater than 5!"
# else:
#   value = "Not greater than 5!"  

# print(value)

########## ########## ########## ########## ##########

# def foo():

#   if inp > 5:
#     value = "Greater than 5!"
#   else:
#     value = "Not greater than 5!"  

# inp = int(input("Enter a number: "))
# foo()

# print(value)

########## ########## ########## ########## ##########

# def add_5(x):
#   x = x + 5
#   print(x)

# x = 10
# print(x)
# add_5(x)
# print(x)

########## ########## ########## ########## ##########

# def append_5(x):
#   x = x[:]
#   x.append(5)
#   print(x)

# x = []
# print(x)
# append_5(x)
# print(x)

########## ########## ########## ########## ##########

value = 5

def foo():
  # global value
  value = 10

print(value)
foo()
print(value)

# value = 20
# foo()