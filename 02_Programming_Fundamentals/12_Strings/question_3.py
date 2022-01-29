# Write a program that asks the user to input two words and 
# determines if the first word is contained in the second one.

##### Sample Program Execution 1 #####
# Enter a word: algo
# Enter another word: algoexpert
# The first word is contained in the second one

##### Sample Program Execution 2 #####
# Enter a word: algo
# Enter another word: algiexpert
# The first word isn't contained in the second one

# You'll have to use the following strings:
# 1) "Enter a word: "
# 2) "Enter another word: "
# 3) "The first word is contained in the second one"
# 4) "The first word isn't contained in the second one"

word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

if word1 in word2:
    print("The first word is contained in the second one")
else:
    print("The first word isn't contained in the second one")