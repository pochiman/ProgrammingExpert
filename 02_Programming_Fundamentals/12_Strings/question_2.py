# Write a program that asks the user to input an integer.

# If the user inputs a valid integer, the program should ask them for their name, and it 
# should convert their name to all uppercase letters before printing "Hello, _uppercase_name_".

# If the user doesn't input a valid integer, the program should capitalize whatever they entered and print it.

##### Sample Program Execution 1 #####
# Enter an integer: 27
# What is your name? tim
# Hello, TIM

##### Sample Program Execution 2 #####
# Enter an integer: not a number
# Not a number

# You'll have to use the following strings:
# 1) "Enter an integer: "
# 2) "What is your name? "
# 3) "Hello, "

user_input = input("Enter an integer: ")

if user_input.isdigit():
    name = input("What is your name? ")

    print("Hello,", name.upper())
else:
    print(user_input.capitalize())