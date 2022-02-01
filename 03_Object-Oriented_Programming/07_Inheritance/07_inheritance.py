# class Person:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name

#   def say_hello(self):
#     print(f"Hi my name is {self.first_name} {self.last_name}")

# class Employee(Person):
#   def test(self):
#     print("test")

# e = Employee("Tim", "Programmer")
# e = Person("Tim", "Programmer")
# e.say_hello()
# e.test()

########## ########## ########## ########## ##########

# class Person:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name

#   def say_hello(self):
#     print(f"Hi my name is {self.first_name} {self.last_name}")

# class Employee(Person):
#   def say_hello(self):
#     print("------")
#     super().say_hello()
#     print("------")


# p = Person("Joe", "Blank")
# p.say_hello()
# e = Employee("Tim", "Programmer")
# e.say_hello()

########## ########## ########## ########## ##########

# class Person:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name

#   def say_hello(self):
#     print(f"Hi my name is {self.first_name} {self.last_name}")


# class Employee(Person):
#   def __init__(self, first_name, last_name, salary):
#     super().__init__(first_name, last_name)
#     self.salary = salary

#   def say_hello(self):
#     super().say_hello()
#     print(f"My salary is {self.salary}")


# e = Employee("Tim", "Programmer", 50000)
# e.say_hello()

########## ########## ########## ########## ##########

# class Person:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name

#   def say_hello(self):
#     print(f"Hi my name is {self.first_name} {self.last_name}")


# class Employee(Person):
#   def __init__(self, first_name, last_name, salary):
#     super().__init__(first_name, last_name)
#     self.salary = salary

#   def say_hello(self):
#     super().say_hello()
#     print(f"My salary is {self.salary}")


# class Manager(Employee):
#   def __init__(self, first_name, last_name, salary, department):
#     super().__init__(first_name, last_name, salary)
#     self.department = department

# m = Manager("Tim", "Programmer", 50000, "Sports")
# m.say_hello()

# ########## ########## ########## ########## ##########

# class Person:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name

#   def say_hello(self):
#     print(f"Hi my name is {self.first_name} {self.last_name}")


# class Employee(Person):
#   def __init__(self, first_name, last_name, salary):
#     super().__init__(first_name, last_name)
#     self.salary = salary

#   def say_hello(self):
#     super().say_hello()
#     print(f"My salary is {self.salary}")


# class Manager(Employee):
#   def __init__(self, first_name, last_name, salary, department):
#     super().__init__(first_name, last_name, salary)
#     self.department = department


# class Owner(Person):
#   def __init__(self, first_name, last_name, net_worth):
#     super().__init__(first_name, last_name)
#     self.net_worth = net_worth

# o = Owner("Tim", "Programmer", 50000)
# o.say_hello()

########## ########## ########## ########## ##########

# class Person:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name

#   def say_hello(self):
#     print(f"Hi my name is {self.first_name} {self.last_name}")


# class Employee(Person):
#   def __init__(self, first_name, last_name, salary):
#     super().__init__(first_name, last_name)
#     self.salary = salary

#   def say_hello(self):
#     super().say_hello()
#     print(f"My salary is {self.salary}")


# class Manager(Employee):
#   def __init__(self, first_name, last_name, salary, department):
#     super().__init__(first_name, last_name, salary)
#     self.department = department


# class Owner(Person):
#   def __init__(self, first_name, last_name, net_worth):
#     super().__init__(first_name, last_name)
#     self.net_worth = net_worth


# o = Owner("Tim", "Programmer", 50000)
# print(isinstance(o, Person))
# m = Manager("Tim", "Programmer", 50000, "Sports")
# print(isinstance(m, Person))
# m = Manager("Tim", "Programmer", 50000, "Sports")
# print(isinstance(m, Employee))
# m = Manager("Tim", "Programmer", 50000, "Sports")
# print(isinstance(m, Manager))
# m = Manager("Tim", "Programmer", 50000, "Sports")
# print(isinstance(m, Owner))
# p = Person("Tim", "Programmer")
# print(isinstance(p, Owner))

########## ########## ########## ########## ##########

# class A:
  # def __init__(self):
  #   print("A")
#   pass

# class B:
#   def __init__(self):
#     print("B")

# class C(A, B):
#   def __init__(self):
#     super().__init__()

# c = C()
# print(isinstance(c, B))
# print(isinstance(c, A))

########## ########## ########## ########## ##########

class Duck:
  def swim(self):
    print('Swimming duck')

  def fly(self):
    print("Flying duck")

class Whale:
  def swim(self):
    print("Swimming whale")


animals = [Duck(), Duck(), Whale()]

for animal in animals:
  animal.swim()
  animal.fly()