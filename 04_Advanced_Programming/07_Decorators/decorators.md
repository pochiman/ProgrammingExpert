# Key Term

# [Decorator]
`Decorators` describe a special kind of function that is meant to `wrap` another 
function. The canonical example is to write a decorator that is meant to print out 
the time it took for a given function to execute whenever it is called.

A particular `@` notation is used to indicate that a function should be wrapped by 
one or more `decorators`:

`@timer`
`def run_simulation():`
    `...`