# Write a program that asks the user to input five strings and stores them in a list.

# Then, the program should ask the user to input three numbers in the range of 0 to 4,
# inclusive (these numbers will represent list indices).

# Finally, the program should use these numbers to access the three strings at the corresponding 
# indices in the previously created list, concatenate them, and print out the resulting string.

##### Sample Program Execution 1 #####
# Enter a string: tim
# Enter a string: is
# Enter a string: the
# Enter a string: best
# Enter a string: instructor
# Enter a number: 1
# Enter a number: 2
# Enter a number: 4
# istheinstructor

##### Sample Program Execution 2 #####
# Enter a string: tim
# Enter a string: is
# Enter a string: the
# Enter a string: best
# Enter a string: instructor
# Enter a number: 2
# Enter a number: 2
# Enter a number: 2
# thethethe

# You'll have to use the following strings:
# 1) "Enter a string: "
# 2) "Enter a number: "

##### Solution 1 #####
# string1 = input("Enter a string: ")
# string2 = input("Enter a string: ")
# string3 = input("Enter a string: ")
# string4 = input("Enter a string: ")
# string5 = input("Enter a string: ")

# strings = [string1, string2, string3, string4, string5]

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))

# final_string = strings[num1] + strings[num2] + strings[num3]
# print(final_string)

##### Solution 2 #####
# string1 = input("Enter a string: ")
# string2 = input("Enter a string: ")
# string3 = input("Enter a string: ")
# string4 = input("Enter a string: ")
# string5 = input("Enter a string: ")

# strings = []
# strings.append(string1)
# strings.append(string2)
# strings.append(string3)
# strings.append(string4)
# strings.append(string5)

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))

# final_string = strings[num1] + strings[num2] + strings[num3]
# print(final_string)

##### Solution 3 #####
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