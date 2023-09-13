# Key Term

# [*args_and_**kwargs]
Oftentimes, especially when writing `decorators`, you need to write a function that 
can accept any number of arguments (positional and keyword), and perform actions on 
these arguments no matter how many of them there are. By using `*args` and `**kwargs` 
as arguments to your function, you can ensure that the variable `args` and `kwargs` 
will contain all of the previously unused arguments that were passed into your function. 

You must remember that `args` will be a tuple containing all positional arguments that 
were passed, and `kwargs` will be a dictionary containing all of the keyword arguments. 
For instance:

`def add_all_args(*args):`
    `return sum(list(args))`

`print(add_all_args(1, 2, 3, 4, 5))`  # 15  