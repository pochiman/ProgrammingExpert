# Write a program that asks the user to input their favorite programming
# language and outputs a specific string based on their answer.

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