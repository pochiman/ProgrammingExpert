# class Person:
#   def __init__(self, name):
#     self.name = name
#     self._salary = 0

#   def set_salary(self, salary):
#     if salary < 0:
#       raise ValueError("Hey, this is invalid!")
#     self._salary = salary  

#   def get_salary(self):
#     return round(self._salary)

#   salary = property(get_salary, set_salary)

# p = Person("Tim")
# p.set_salary(-15)
# p.set_salary(100)
# p.salary = -100
# p.salary = 101.1111
# print(p.salary)

########## ########## ########## ########## ##########

# class Person:
#   def __init__(self, name):
#     self.name = name
#     self._salary = 0

#   @property
#   def salary(self):
#     return round(self._salary)

#   @salary.setter
#   def salary(self, salary):
#     if salary < 0:
#       raise ValueError("Hey, this is invalid!")
#     self._salary = salary  

  # salary = property(get_salary, set_salary)

# p = Person("Tim")
# p.salary = 101.1111
# print(p.salary)

########## ########## ########## ########## ##########

class Time:
  def __init__(self, second):
    self._second = second

  @property
  def second(self):
    print("run")
    return self._second

  @second.setter
  def second(self, second):
    if second < 0 or second > 60:
      raise ValueError("Invalid!")
    self._second = second

t = Time(54)
t.second = 59
print(t.second)

########## ########## ########## ########## ##########

class Time:
  def __init__(self, second):
    self._second = second

  def get_second(self):
    print("run")
    return self._second

  def set_second(self, second):
    if second < 0 or second > 60:
      raise ValueError("Invalid!")
    self._second = second

  second = property(get_second, set_second)

t = Time(54)
t.second = 59
print(t.second)