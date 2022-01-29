##### Sort Employees #####
# Write a function that accepts a list of lists that contain the name, age and salary of specific employees 
# and also accepts a string representing the key to sort employees by.  Your function should return a new 
# list that contains the lists representing each employee sorted in ascending order by the given key.

# The string parameter named sort_by will always be equal to one of the following values: 
# "name", "age" or "salary".

# See the sample input and output below for a detailed example.

##### Sample Input 1 #####
# employees = 
# [
#   ["John", 33, 65000],
#   ["Sarah", 24, 75000],
#   ["Josie", 29, 100000],
#   ["Jason", 26, 55000],
#   ["Connor", 25, 110000]
# ]
# sort_by = "age"

##### Sample Output 1 #####
# [
#   ["Sarah", 24, 75000],
#   ["Connor", 25, 110000],
#   ["Jason", 26, 55000],
#   ["Josie", 29, 100000],
#   ["John", 33, 65000]
# ]

##### Sample Input 2 #####
# employees = 
# [
#   ["John", 33, 65000],
#   ["Sarah", 24, 75000],
#   ["Josie", 29, 100000],
#   ["Jason", 26, 55000],
#   ["Connor", 25, 110000]
# ]
# sort_by = "salary"

##### Sample Output 2 #####
# [
#   ["Jason", 26, 55000],
#   ["John", 33, 65000],
#   ["Sarah", 24, 75000],
#   ["Josie", 29, 100000],
#   ["Connor", 25, 110000]
# ]

##### Sample Input 3 #####
# employees = 
# [
#   ["John", 33, 65000],
#   ["Sarah", 24, 75000],
#   ["Josie", 29, 100000],
#   ["Jason", 26, 55000],
#   ["Connor", 25, 110000]
# ]
# sort_by = "name"

##### Sample Output 3 #####
# [
#   ["Connor", 25, 110000],
#   ["Jason", 26, 55000],
#   ["John", 33, 65000],
#   ["Josie", 29, 100000],
#   ["Sarah", 24, 75000]
# ]

##### Solution 1 #####
# def sort_employees(employees, sort_by):
#     sort_indices = ["name", "age", "salary"]
#     sort_index = sort_indices.index(sort_by)

#     sorted_employees = []
#     # Copy the employees list so we don't modify it
#     employees_copy = employees[:]

#     while len(employees_copy) > 0:
#         smallest_employee_index = 0

#         for i, employee in enumerate(employees_copy):
#             current_smallest_value = employees_copy[smallest_employee_index][sort_index]
#             if employee[sort_index] < current_smallest_value:
#                 smallest_employee_index = i

#         # After looking through all remaining employees we will have found the employee
#         # with the smallest sort_by value so we add it to the sorted list
#         next_sorted_employee = employees_copy[smallest_employee_index]
#         sorted_employees.append(next_sorted_employee)
#         employees_copy.pop(smallest_employee_index)

#     return sorted_employees

##### Solution 2 #####
def sort_employees(employees, sort_by):
    sort_indices = ["name", "age", "salary"]
    sort_index = sort_indices.index(sort_by)

    sorted_employees = sorted(employees, key=lambda x: x[sort_index])

    return sorted_employees