# Key Terms

# [Class_Attribute]
An `attribute` is an `object` that belongs either to a class, or to an instance 
of that class. Attributes of an object can be referenced using the `.` notation: 
`print(person.name)`.

A `class attribute` is an attribute that is associated with a class, not an instance 
of a class. Class attributes can be modified and accessed by using the class name 
directly or by using an instance of the class. Typically, class attributes are 
defined at the top of the class, inside the class body.

# [Class_Method]
A `class method` is a method that has a mandatory `cls` parameter and can only access 
class attributes and other class methods. It does not act on an instance of a class, 
but on the class itself. Class methods are denoted with the `@classmethod` decorator.