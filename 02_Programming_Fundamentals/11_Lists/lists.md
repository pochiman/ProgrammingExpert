# Key Terms

# [List]
In Python, a list is a data type that stores an ordered collection of elements. 
You can access individual elements in a list using their indices and add elements 
to a list by using the `.append(item)` method. Example:

`lst = [1, 10, 4, True, "str"]`
`lst.append(2)`   # lst is now equal to [1, 10, 4, True, "str", 2]
`print(lst[1])`   # this outputs 10
`print(lst[-1])`  # this outputs 2

# [In]
The in keyword in Python lets you check whether a value is contained in a collection 
(such as a `list`, `set`, `dict`, etc).

`print("hello" in ["hello", "world"])`  # True

The `in` keyword can also be used to iterate over the items in a collection when 
using a `for` loop.