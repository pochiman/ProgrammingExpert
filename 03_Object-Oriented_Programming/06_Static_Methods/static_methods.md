# Key Term

# [Static_Method]
A `static` method is defined within a class but should not reference anything relevant 
to that class specifically, except for other static methods.

For the most part, static methods should only be used for `pure` functions, which do 
not use temporary variables outside of their own scope and exclusively transform a 
set of inputs into some outputs. For instance, a method that converts a distance from 
kilometers to miles should most likely be `static`. Static methods are denoted using 
the `@staticmethod` decorator.