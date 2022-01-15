# Write a program that asks the user to input five strings and stores them in a list.

# Then, the program should ask the user to input three numbers in the range of 0 to 4,
# inclusive (these numbers will represent list indices).

# Finally, the program should use these numbers to access the three strings at the corresponding 
# indices in the previously created list, concatenate them, and print out the resulting string.

# You'll have to use the following strings:
# 1) "Enter a string: "
# 2) "Enter a number: "

strings = [
    input("Enter a string: "),
    input("Enter a string: "),
    input("Enter a string: "),
    input("Enter a string: "),
    input("Enter a string: "),
]

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

final_string = strings[num1] + strings[num2] + strings[num3]
print(final_string)