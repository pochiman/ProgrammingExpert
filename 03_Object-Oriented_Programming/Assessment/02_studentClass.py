##### Student Class #####

# Write a Student class, as defined below, that keeps track of all created students.

# Your class should implement the following methods, class variables and properties:

##### An instance attribute called name.

##### A property called grade that returns the grade of that student.  Trying to set the 
##### grade should raise a ValueError if the new grade is not a number between 0 and 100.

##### A static method called calculate_average_grade(students) that accepts a list of Student objects and 
##### returns the average grade for those students.  If there are no students in the list, it should return -1.

##### A class variable called all_students that stores all of the student objects that have been created in a list.

##### A class method named get_average_grade() which returns the average grade of all created students.

##### A class method named get_best_student() which returns the student object with the best grade out of 
##### all the currently created students.  If there are no students created, this method should return None.
##### You may assume there will always be one student with the best grade, except in the case where there are 
##### no students created.

# See below for an example of the behavior of the Student class.

# >>> Student.get_average_grade()
# -1
# >>> student1 = Student("Antoine", 75)
# >>> student1.name
# "Antoine"
# >>> student1.grade
# 75
# >>> student1.grade = 150
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: New grade not in the accepted range of [0-100].
# >>> student1 == Student.get_best_student()
# True

class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if new_grade < 0 or new_grade > 100:
            raise ValueError("New grade not in the accepted range of [0-100].")
        self._grade = new_grade

    @classmethod
    def get_best_student(cls):
        best_student = None
        for student in cls.all_students:
            if best_student == None or best_student.grade < student.grade:
                best_student = student
        return best_student

    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_students)

    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1

        total = 0
        for student in students:
            total += student.grade
        return total / len(students)