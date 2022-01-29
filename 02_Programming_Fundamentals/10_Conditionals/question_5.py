# Write a program that asks the user to input their favorite programming
# language and outputs a specific string based on their answer.

##### Sample Program Execution 1 #####
# What's your favorite programming language? Python
# Nice choice!

##### Sample Program Execution 2 #####
# What's your favorite programming language? Golang
# You're a cool kid I see...

##### Sample Program Execution 3 #####
# What's your favorite programming language? JavaScript
# Okay Mr. web developer.

##### Sample Program Execution 4 #####
# What's your favorite programming language? Any other text
# I don't know that language.

# You'll have to use the following strings:
# 1) "What's your favorite programming language? "
# 2) For Python, "Nice choice!"
# 3) For Golang, "You're a cool kid I see..."
# 4) For JavaScript, "Okay Mr. web developer."
# 5) For anything else, "I don't know that language."

fav_language = input("What's your favorite programming language? ")

if fav_language == "Python":
  print("Nice choice!")
elif fav_language == "Golang":
  print("You're a cool kid I see...")
elif fav_language == "JavaScript":
  print("Okay Mr. web developer.")
else:
  print("I don't know that language.")