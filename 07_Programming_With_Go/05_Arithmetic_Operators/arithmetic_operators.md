# Key Term

# [Integer_Overflow]
In programming, an `integer overflow` occurs when an arithmetic operation tries to create 
a value that is outside of the acceptable range. Take the following as an example:

`var result uint8 = 250 + 8`

This code would result in an overflow because the maximum value that can be stored in a 
variable of `uint8` is `255` and `250 + 8 = 258`.