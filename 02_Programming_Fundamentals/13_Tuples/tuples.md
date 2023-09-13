# Key Term

# [Tuple]
A `tuple` is similar to a list in that it stores a collection of elements. Like 
lists, you can access individual elements in a tuple using their indices, but 
you cannot modify or change these elements. Example:

`tup = (1, 10, 4, True, "str")`
`print(tup[1])`   # this outputs 10
`print(tup[-1])`  # this outputs "str"
`tup[1] = 0`      # this raises an exception
`tup.append(1)`   # this raises an exception