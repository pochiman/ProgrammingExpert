# Write a program that asks the user to input a sentence 
# and outputs how many words are in the sentence.

# Try using an f-string to embed the number of words in your output, 
# and don't worry about singularization when there's only one word.

# You'll have to use the following strings:
# 1) "Enter a sentence: "
# 2) "There are _ words in this sentence"

sentence = input("Enter a sentence: ")

words = sentence.split(" ")
number_of_words = len(words)

print(f"There are {number_of_words} words in this sentence")