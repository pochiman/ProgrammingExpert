# def foo(x):
#   print(x)

# print(type(foo))
# def call_func(func, x):
#   func(x)

# call_func(foo, 7)

########## ########## ########## ########## ##########

# def outer(x):
#   def inner(y):
#     print(x + y)

#   return inner

# x = outer(5)
# print(x)
# func = outer(5)
# func(6)
# func(3)
# func2 = outer(1)
# func2(1)

########## ########## ########## ########## ##########

# def outer(x):
#   def inner(y):
#     print(x + y)

#   inner(5)

# outer(5)

########## ########## ########## ########## ##########

# def outer(x):
#   def inner(y):
#     def inner2(z):
#       print(x + y + z)

#     return inner2

#   return inner

# outer(5)(5)(5)

########## ########## ########## ########## ##########

# def outer(x):
#   def inner():
#     print(x)

#   return inner

# func = outer(5)
# func()

########## ########## ########## ########## ##########

# def collection():

#   lst = []

#   def inner(value):
#     lst.append(value)
#     return lst

#   return inner

# add_value = collection()
# print(add_value(1))
# print(add_value(2))
# print(add_value(3))
# print(add_value(4))

########## ########## ########## ########## ##########

# class Collection:
#   def __init__(self):
#     self.lst = []

#   def add_value(self, value):
#     self.lst.append(value)
#     return self.lst  

# def collection():

#   lst = []

#   def inner(value):
#     lst.append(value)
#     return lst

#   return inner

# add_value = collection()
# print(add_value(1))
# print(add_value(2))
# print(add_value(3))
# print(add_value(4))

########## ########## ########## ########## ##########

# class Counter:
#   def __init__(self, start):
#     self.count = start

#   def count(self, value):
#     self.count += value
#     return self.count

# def counter(start):
#   count = start

#   def increment(value):
#     nonlocal count
#     count += value
#     return count

#   return increment

# count = counter(2)
# print(count(1))
# print(count(1))    
# print(count(1))

########## ########## ########## ########## ##########

def outer():
  def inner():
    nonlocal x

    def inner2():
      nonlocal x
      x = 2
      print("Inner2:", x)

    x = 3
    inner2()
    print("Inner:", x)

  x = 4
  inner()
  print("Outer:", x)

outer()