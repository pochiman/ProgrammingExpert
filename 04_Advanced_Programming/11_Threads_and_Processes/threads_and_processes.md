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

# [Process]
A `process` is an application or program that is running on your computer. 
Processes are allocated their own memory space and always contain at least one 
thread, but may be split into multiple threads that are executing concurrently.

# [Concurrency]
`Concurrency` refers to the ability for parts of a program, application or 
algorithm (i.e. multiple threads) to be executed simultaneously.

# [Parallelism]
`Parallelism` refers to several computations occuring at the same time. Parallel 
programs utilize multiple logical processing cores of your CPU to increase speed. 
This is different from a concurrent program that may only utilize a single logical 
CPU core.