# def gen():
#   yield 1
#   yield 2
#   yield 3

# print(type(gen))
# print(type(gen()))
# print(gen())

########## ########## ########## ########## ##########

# def gen():
#   yield 1
#   yield 2
#   yield 3

# itr = gen()

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

########## ########## ########## ########## ##########

# def gen():
#   yield 1
#   yield 2
#   yield 3

# itr = gen()

# for i in itr:
#   print(i)

########## ########## ########## ########## ##########

def fib(n):
  # 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21
  last = 1
  second_last = 1
  current = 3 # 4

  while current <= n:
    num = last + second_last # 3
    yield num

    second_last = last # 1
    last = num # 2
    current += 1

for val in fib(10):
  print(val)

'''
fib_numbers = [1, 1]

for i in range(2, 10):
  last = fib_numbers[i - 1]
  second_last = fib_numbers[i - 2]
  num = last + second_last
  fib_numbers.append(num)

print(fib_numbers)
'''