##### Reading Files #####

# Open a file named "programmingExpert.txt" that is located in the data directory 
# and print how many words are present in the file.

# Escape characters like \n and \t, periods, commas and dashes (-) are not considered words.
# You may assume that all other text in the file that is separated by a space is a word.

##### Solution 1 #####
# text = ""

# with open("data/programmingExpert.txt", "r") as file:
#     text = file.read()

# escape_characters_removed = text.replace("\n", " ")
# punctuation_removed = escape_characters_removed.replace(
#     ",", "").replace("-", "").replace(".", "")

# words = punctuation_removed.split(" ")
# empty_strings = words.count("")
# number_of_words = len(words) - empty_strings

# print(number_of_words)

##### Solution 2 #####
file = open("data/programmingExpert.txt", "r")
text = file.read()
file.close()

escape_characters_removed = text.replace("\n", " ")
punctuation_removed = escape_characters_removed.replace(
    ",", "").replace("-", "").replace(".", "")

words = punctuation_removed.split(" ")
empty_strings = words.count("")
number_of_words = len(words) - empty_strings

print(number_of_words)