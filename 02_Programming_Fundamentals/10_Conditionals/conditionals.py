if True:
   print("If statement ran")

##### ##### ##### ##### #####

name = input("Name: ")

if name == "Tim":
    print("Hello Tim!")
    print("Hello Tim!")

##### ##### ##### ##### #####

number = float(input("Enter a number below 5: "))

if number < 5:
    print("good job!")
else:
    print("not a good job!")

print("Finished!")

##### ##### ##### ##### #####

number = float(input("Enter a number: "))

if number < 0:
    print("This is a negative number")
elif number < 10:
    print("This is less than 10")
elif number < 20:
    print("This is less than 20")  
else:
    print("not a good job!")

##### ##### ##### ##### #####

number = float(input("Enter a number: "))

if number > 0 and number % 2 == 0:
    print("This is a positive even number!")
    
    number2 = float(input("Number: "))
    if number2 < 0:
        print("This is a negative")
    else:
        print("This is a positive")

##### ##### ##### ##### #####

# This is a one-line if statement.
# You use this because you want to assign a value to a variable based on a condition, 
# or you wanna do something based on a condition and it's just in one line. 
x = 5

# So again, this is what you want if the condition is true, 
# and this is what you want if the condition is not true.
result = "Ok" if x > 5 else "Not Ok"
print(result)

##### ##### ##### ##### #####

# You can also put statements for single in-line if statements. 
print("Hello") if x > 5 else print("Not okay")