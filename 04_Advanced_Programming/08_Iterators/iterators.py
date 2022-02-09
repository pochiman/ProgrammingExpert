# x = [1, 2, 3]

# for val in x:
#   print(val)

# x_iter = iter(x)
# print(x_iter)
# print(next(x_iter))
# print(next(x_iter))
# print(next(x_iter))
# print(next(x_iter))

########## ########## ########## ########## ##########

# x = [1, 2, 3]

# x_iter = iter(x)

# while True:
#   try:
#     print(next(x_iter))
#   except StopIteration:
#     break

########## ########## ########## ########## ##########

# x = [1, 2, 3]

# x_iter = x.__iter__()

# while True:
#   try:
#     print(x_iter.__next__())
#   except StopIteration:
#     break

########## ########## ########## ########## ##########

# class Numbers:
#   def __init__(self, num1, num2, num3):
#     self.num1 = num1
#     self.num2 = num2
#     self.num3 = num3

#   def __iter__(self):
#     return NumberIterator(self.num1, self.num2, self.num3)

# class NumberIterator:
#   def __init__(self, one, two, three):
#     self.one = one
#     self.two = two
#     self.three = three
#     self.current = 0

#   def __next__(self):
#     self.current += 1
#     if self.current == 1:
#       return self.one
#     elif self.current == 2:
#       return self.two
#     elif self.current == 3:
#       return self.three
#     else:
#       raise StopIteration

# nums = Numbers(1, 2, 3)
# itr = iter(nums)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# for num in nums:
#   print(num)

########## ########## ########## ########## ##########

class Numbers:
  def __init__(self, num1, num2, num3):
    self.num1 = num1
    self.num2 = num2
    self.num3 = num3
    self.current = 0

  def __iter__(self):
    self.current = 0
    return self

  def __next__(self):
    self.current += 1

    if self.current == 1:
      return self.num1
    elif self.current == 2:
      return self.num2
    elif self.current == 3:
      return self.num3
    else:
      raise StopIteration

nums = Numbers(1, 2, 3)
num_iter_1 = iter(nums)
print(next(num_iter_1))

num_iter_2 = iter(nums)
print(next(num_iter_1))
print(next(num_iter_2))
print(next(num_iter_1))

# for val in nums:
#   print(val)