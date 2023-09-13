# Key Term

# [Exception]
An `exception` in Python is `raised` when something unexpected happens during the 
execution of your program. For instance, if you try to convert the string `"hello"` 
into an `integer`, your program will raise a `ValueError`.

If you anticipate that a part of your code might, in some cases, raise an exception, 
you can surround that part of the code with a `try/except` block and prevent your 
program from completely crashing.

`try:`
    `i = int("hello")`
`except Exception as e:`
    `print(f"Caught the exception: {e}")`