# Write a program that asks a user for two numbers: a numerator and a denominator.  Your program should
# divide the numerator by the denominator and handle any exceptions that might occur during the division.

# Specifically, your program should catch exceptions when either the numerator or the denominator isn't a number and when
# the denominator is 0 (you can't divide by 0).  All exceptions should be caught and handled, even when there are multiple.

# If the division doesn't raise any exceptions, the program should print the result of the division.
# And regardless of outcome, the program should tell the user goodbye!

##### Sample Program Execution 1 #####
# Enter the numerator: 5
# Enter the denominator: 0
# You cannot divide by 0.
# This division cannot be performed.
# Goodbye!

##### Sample Program Execution 2 #####
# Enter the numerator: hello
# Enter the denominator: 2
# The numerator is not a number.
# This division cannot be performed.
# Goodbye!

##### Sample Program Execution 3 #####
# Enter the numerator: 3
# Enter the denominator: 7.h
# The denominator is not a number.
# This division cannot be performed.
# Goodbye!

##### Sample Program Execution 4 #####
# Enter the numerator: h
# Enter the denominator: 7.h
# The numerator is not a number.
# The denominator is not a number.
# This division cannot be performed.
# Goodbye!

##### Sample Program Execution 5 #####
# Enter the numerator: 4
# Enter the denominator: 2.0
# The result of this division is 2.0.
# Goodbye!

# You'll have to use the following strings:
# 1) "Enter the numerator: "
# 2) "Enter the denominator: "
# 3) "The numerator is not a number."
# 4) "The denominator is not a number."
# 5) "You cannot divide by 0."
# 6) "This division cannot be performed."
# 7) "The result of this division is _."
# 8) "Goodbye!"

##### Solution 1 #####
# numerator = input("Enter the numerator: ")
# denominator = input("Enter the denominator: ")

# try:
#     numerator = float(numerator)
# except Exception as e:
#     print("The numerator is not a number.")

# try:
#     denominator = float(denominator)
# except Exception as e:
#     print("The denominator is not a number.")


# try:
#     result = numerator / denominator
#     print(f"The result of this division is {result}.")
# except ZeroDivisionError as e:
#     print("You cannot divide by 0.")
#     print("This division cannot be performed.")
# except Exception as e:
#     print("This division cannot be performed.")
# finally:
#     print('Goodbye!')

##### Solution 2 #####
numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

try:
    numerator = float(numerator)
except Exception as e:
    print("The numerator is not a number.")

try:
    denominator = float(denominator)
    if denominator == 0:
        print("You cannot divide by 0.")
except Exception as e:
    print("The denominator is not a number.")


try:
    result = numerator / denominator
    print(f"The result of this division is {result}.")
except Exception as e:
    print("This division cannot be performed.")
finally:
    print('Goodbye!')