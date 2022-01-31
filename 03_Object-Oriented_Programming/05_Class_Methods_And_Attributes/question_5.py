##### Employee Class #####

# Create an Employee class where each employee has a name, age and salary.  This class should contain 
# two class attributes that store the average employee age and salary.  These class attributes should 
# be named average_age and average_salary and should be updated each time a new employee is created.

# Note: you may add as many other additional attributes as you like.

# See below for an example.

# >>> e1 = Employee("George", 34, 65000)
# >>> print(Employee.average_age)
# 34.0
# >>> print(Employee.average_salary)
# 65000.0
# >>> e2 = Employee("Sarah", 25, 95000)
# >>> print(Employee.average_age)
# 29.5
# >>> print(Employee.average_salary)
# 80000.0

class Employee:
    number_of_employees = 0
    average_age = 0
    average_salary = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        total_age = Employee.average_age * Employee.number_of_employees
        total_salary = Employee.average_salary * Employee.number_of_employees
        Employee.average_age = (total_age + age) / (Employee.number_of_employees + 1)
        Employee.average_salary = (total_salary + salary) / (Employee.number_of_employees + 1)
        Employee.number_of_employees += 1