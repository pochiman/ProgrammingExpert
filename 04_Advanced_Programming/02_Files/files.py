# file = open("04_Advanced_Programming/02_Files/file.txt", "r")
# print(file.read())
# file.close()

########## ########## ########## ########## ##########

# with open("04_Advanced_Programming/02_Files/file.txt", "r") as file: 
#   print(file.read())

########## ########## ########## ########## ##########

# with open("04_Advanced_Programming/02_Files/file.txt", "r") as file: 
#   print(file.readlines())

########## ########## ########## ########## ##########

# with open("04_Advanced_Programming/02_Files/file.txt", "r") as file: 
#   line1 = file.readlines()[0]
  # print([line1])
  # print([line1.strip()])

########## ########## ########## ########## ##########

# with open("04_Advanced_Programming/02_Files/file.txt", "r") as file: 
#   line1 = file.read()
#   line1 = line1.replace("\n", "")
#   print([line1])

########## ########## ########## ########## ##########

# with open("04_Advanced_Programming/02_Files/file2.txt", "w") as file: 
#   file.write("hello!\n")
#   file.write("hello!\n")
#   file.write("hello!")

########## ########## ########## ########## ##########

# with open("04_Advanced_Programming/02_Files/file2.txt", "a") as file: 
#   file.write("\nhello!\n")
#   file.write("hello!\n")
#   file.write("hello!")

########## ########## ########## ########## ##########

# with open("04_Advanced_Programming/02_Files/file2.txt", "r+") as file: 
#   file.write("\ntest!")

########## ########## ########## ########## ##########

# with open("04_Advanced_Programming/02_Files/file2.txt", "r+") as file: 
#   score = file.read()
#   new_score = int(score) + 1
#   file.seek(0)
#   file.write(str(new_score))

########## ########## ########## ########## ##########

# with open("04_Advanced_Programming/02_Files/file2.txt", "r+") as file: 
  # lines = file.readlines()[:3]
  # for line in file:
  #   print(line, end="")

########## ########## ########## ########## ##########

# with open("04_Advanced_Programming/02_Files/file2.txt", "r+") as file: 

#   count = 0
#   for line in file:
#     print(line, end="")
#     count += 1
#     if count >= 3:
#       break

########## ########## ########## ########## ##########

# with open("04_Advanced_Programming/02_Files/file2.txt", "r+") as file: 

#   for i, line in enumerate(file):
#     print(line, end="")
#     if i == 2:
#       break

########## ########## ########## ########## ##########

with open("04_Advanced_Programming/02_Files/file2.txt", "r+") as file: 

  # print(file.read(5))
  print(file.read(7))  