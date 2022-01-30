# class Person:
#   def __init__(self, name):
#     self.name = name

#   def say_hello(self):
#     print(f"Hello, {self.name}")

#   def set_age(self, age):
#     self.age = age

#   def get_age(self):
#     return self.age  


# p1 = Person("Tim")
# p2 = Person("Susan")
# p1.set_age(21)
# p1.say_hello()
# p2.say_hello()
# print(p1.age)
# print(p1.get_age())

########## ########## ########## ########## ##########

# class Person:
#   def __init__(self, name):
#     self.name = name
#     self.age = None

#   def say_hello(self):
#     print(f"Hello, {self.name}")

#   def set_age(self, age):
#     self.age = age

#   def get_age(self):
#     return self.age  


# p1 = Person("Tim")
# p2 = Person("Susan")
# p1.set_age(24)
# p1.age
# print(p1.get_age())

########## ########## ########## ########## ##########

# class Counter:
#   def __init__(self):
#     self.count = 0

#   def increment(self):
#     self.count += 1

#   def decrement(self):
#     self.count -= 1

#   def print_count(self):
#     print(f"The current count is {self.count}")

# counter = Counter()
# counter.increment()
# counter.decrement()
# counter.print_count()
# counter.increment()
# counter.increment()
# counter.print_count()

########## ########## ########## ########## ##########

# class Counter:
#   def __init__(self):
#     self.count = 0
#     self.locked = False

#   def toggle_lock(self):
#     self.locked = not self.locked

#   def increment(self):
#     if self.locked:
#       raise Exception("The counter is locked!")
#     self.count += 1

#   def decrement(self):
#     if self.locked:
#       raise Exception("The counter is locked!")
#     self.count -= 1

#   def print_count(self):
#     print(f"The current count is {self.count}")

# counter = Counter()

# counter.increment()
# counter.increment()
# counter.increment()
# counter.decrement()
# counter.print_count()

# counter.toggle_lock()
# counter.decrement()

########## ########## ########## ########## ##########

class Counter:
  def __init__(self):
    self.count = 0
    self.locked = False

  def toggle_lock(self):
    self.locked = not self.locked

  def increment(self):
    if self.locked:
      raise Exception("The counter is locked!")
    self.count += 1

  def decrement(self):
    if self.locked:
      raise Exception("The counter is locked!")
    self.count -= 1

  def print_count(self):
    print(f"The current count is {self.count}")

counter = Counter()
counter2 = Counter()

counter.toggle_lock()
counter2.increment()
counter.print_count()
counter2.print_count()