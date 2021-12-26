# Write a program that asks the user to input any number.

# If the number is between 10 and 20, your program should ask the user
# to enter another number and then print the sum of the two numbers.
# If the sum is over 100, your program should also print "That is a large sum!" on a new line.

# If the user doesn't enter a number between 10 and 20, your program shouldn't print anything.

number1 = float(input("Enter a number: "))
# we use float() instead of int() to make sure if the user
# enters a float like: 2.1, 0.3 or 4.5 the program doesn't crash

if number1 >= 10 and number1 <= 20:
    number2 = float(input("Enter another number: "))
    sum_of_numbers = number1 + number2

    print("The sum of these two numbers is:", sum_of_numbers)

    if sum_of_numbers > 100:
        print("That is a large sum!")