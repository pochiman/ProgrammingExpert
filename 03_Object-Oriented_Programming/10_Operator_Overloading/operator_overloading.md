# Key Term

# [Dunder_Method]
Dunder methods are methods that are prefixed and suffixed by two underscores. The 
most important to know is the `__init__` dunder method, which is sometimes called 
the `constructor` of the class, and defines how a new instance is initialized after 
being created.

Implementing those methods will sometimes change how certain operators will behave 
(like `+` with `__add__` and `==` with `__eq__`). Other examples include `__len__`, 
`__str__`, `__repr__` and many more.