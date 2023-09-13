# Key Term

# [Lambda]
A `lambda` is an anonymous function that can be defined in-line without the use of 
the `def` keyword. This is extremely useful when defining a custom sort ordering 
for a collection. Example:

`# Here we have a list of tuples,`
`# each representing a food and its price.`
`lst = [`
    `('cake','30'),`
    `('orange','3'),`
    `('pasta','20'),`
`]`

`# This lambda function lets us sort`
`# by the price of the items.`
`lst.sort(key=lambda x:x[1])`