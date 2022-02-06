# func = lambda x, y, z=0: x + y + z
# func = lambda x, y, z=0: print(x + y + z)
# print(func(1, 2, 4))
# func(1, 2, 4)

########## ########## ########## ########## ##########

# def sort_func(x):
#   return x[1]

# lst = [(1, 2), (-2, -4), (3, 4), (0, 0)]
# lst.sort(key=sort_func)
# print(lst)

########## ########## ########## ########## ##########

# lst = [(1, 2), (-2, -4), (3, 4), (0, 0)]
# lst.sort(key=lambda x: x[1])
# print(lst)

########## ########## ########## ########## ##########

# mul = lambda x: lambda y: x * y

# result = mul(2)
# print(result(4))

########## ########## ########## ########## ##########

def mul(x):
  def mul2(y):
    return x * y

  return mul2

# result = mul(5)
result = mul(5)(4)
# print(result(2))
print(result)