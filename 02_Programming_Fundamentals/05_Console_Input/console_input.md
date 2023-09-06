# Key Term

# [Input]
The `input` function is built directly into Python as a means to gather user input from the command line.

An important note is that it will always return a `str` object which will need to be converted to an `int`
(for example) if you expect the user input to be an integer.

`user_name = input("What is your name? ")`
`print("Hello", user_name + "!")`