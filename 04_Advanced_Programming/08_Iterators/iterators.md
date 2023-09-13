# Key Term

# [Iterator]
An `iterator` is a special kind of object that implements a single function: `next()`. 
Iterators historically were created through class definitions which had to implement 
the `__iter__()` method to create the iterator, in addition to the `__next__()` method. 
However, most modern programmers opt to use the `generator` syntax nowadays due to 
increased readability and conciseness.