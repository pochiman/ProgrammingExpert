# Write a program that continually asks the user to enter a number until they enter the 
# number 5, at which point the program should print how many numbers the user has entered.

##### Sample Program Execution #####
# Enter a number: 4
# Enter a number: 3
# Enter a number: 5
# You entered 3 numbers.

# You'll have to use the following strings:
# 1) "Enter a number: "
# 2) "You entered _ numbers."

number_of_entries = 0

while True:
    number = int(input("Enter a number: "))
    number_of_entries += 1

    if number == 5:
        break

print(f"You entered {number_of_entries} numbers.")