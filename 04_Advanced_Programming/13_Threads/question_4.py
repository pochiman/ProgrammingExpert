##### Foo Bar Multi-threaded #####

# Write a program that asks the user to input a positive integer n and uses multiple threads to print 
# "foo" then "bar" alternatively n times.  Your program should print everything on the same line.

# Your program must use at least 2 threads, one thread responsible for printing "foo" and another for printing "bar".

# You may assume the input from the user for n will always be a positive integer.

##### Sample Program Execution #####
# Enter a positive integer: 4
# "foobarfoobarfoobarfoobar"

import threading


def print_foo(n, foo_lock, bar_lock):
    for _ in range(n):
        foo_lock.acquire()
        print("foo", end="")
        bar_lock.release()


def print_bar(n, foo_lock, bar_lock):
    for _ in range(n):
        bar_lock.acquire()
        print("bar", end="")
        foo_lock.release()


n = int(input("Enter a positive integer: "))

foo_lock = threading.Lock()
bar_lock = threading.Lock()
bar_lock.acquire()

foo_thread = threading.Thread(target=print_foo, args=(n, foo_lock, bar_lock))
bar_thread = threading.Thread(target=print_bar, args=(n, foo_lock, bar_lock))

foo_thread.start()
bar_thread.start()

foo_thread.join()
bar_thread.join()