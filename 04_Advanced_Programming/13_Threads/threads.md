# Key Terms

# [Thread]
A `thread` is a flow of execution of your program. By default, Python will run your 
program in a single thread, the `main` thread, which will execute your Python code 
line by line.

When trying to speed up certain programs using `concurrency`, many programs choose 
to run multiple threads at the same time. The `threading` package that comes pre-
installed contains functions and classes that allow you to create new threads and 
coordinate them.

The most important elements of this library are: `Thread` and `Lock`.

# [Concurrency]
`Concurrency` refers to the ability for parts of a program, application or algorithm 
(i.e. multiple threads) to be executed simultaneously.

# [Mutex]
A `mutex` is a `mutually exclusive lock` that controls the access to a section of 
code. Mutex's are typically used in multi-threaded programs when a section of code 
should only be executed by one thread at a time. If one thread has acquired the 
mutex, all other threads must wait until that thread releases it before they can 
execute that locked section of code.