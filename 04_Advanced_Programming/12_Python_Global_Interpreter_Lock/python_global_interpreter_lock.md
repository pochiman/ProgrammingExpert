# Key Term

# [Mutex]
A `mutex` is a `mutually exclusive lock` that controls the access to a section of 
code. Mutex's are typically used in multi-threaded programs when a section of code 
should only be executed by one thread at a time. If one thread has acquired the 
mutex, all other threads must wait until that thread releases it before they can 
execute that locked section of code.