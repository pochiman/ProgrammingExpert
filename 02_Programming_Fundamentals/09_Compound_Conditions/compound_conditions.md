# Key Terms

# [And_/_Or_/_Not]
When you want to create larger conditions based on multiple smaller conditions, 
you will need to use the `and`, `or`, `not` keywords. Conditions that contain 
these keywords are called `compound conditions`.

`if x == 1 and y == 2:`
    `print("x is equal to 1 and y is equal to 2")`
`elif not (x == 2 or y == 2):`
    `print("neither x and y are equal to 2")`

# [De_Morgan's_Laws]
`De Morgan's laws` state:

 • `not (x and y) == not x or not y`
 • `not (x or y) == not x and not y`

 You can use these laws to simplify complex conditions.