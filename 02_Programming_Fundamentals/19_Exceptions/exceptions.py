# try:
#   int("hello")
# except:
#   print("Exception!")

# print("Done")

########## ########## ########## ########## ##########

# try:
#   int("hello")
# except ValueError as e:
#   print("Exception!", e)

# print("Done")

########## ########## ########## ########## ##########

# try:
#   2 / 0
#   int("hello")
# except ValueError as e:
#   print("Value Exception!", e)
# except ZeroDivisionError as e:
#   print("Zero Div Exception!", e)  

# print("Done")

########## ########## ########## ########## ##########

# try:
#   2 / 0
#   int("hello")
# except Exception as e:
#   print("Exception!", e)

# print("Done")

########## ########## ########## ########## ##########

# try:
#   2 / 0
#   int("hello")
#   int(1)
# except Exception as e:
#   print("Exception!", e)
# finally:
#   print("Done")

########## ########## ########## ########## ##########

# try:
#   x = [1, 2, 4, 3]
#   x[3] = 2 # mystery line
# except Exception as e:
#   print("Exception!", e)
# finally:
#   x = [1, 2, 4, 3]
#   print("Done")

########## ########## ########## ########## ##########

# x = []
# x = {}
# x[1]

########## ########## ########## ########## ##########

# raise ValueError("This is an error!")
# raise Exception("This is an error!")
# raise IndexError("This is an error!")

########## ########## ########## ########## ##########

# num = input("Enter a number: ")

# if not num.isdigit():
#   raise ValueError("This is not a valid number!")

########## ########## ########## ########## ##########

# while True:
#   num = input("Enter a number: ")

#   try:
#     num = float(num)
#     break
#   except ValueError:
#     print("Not a valid float, try again!")

########## ########## ########## ########## ##########

num = input("Enter a number: ")
num = float(num)