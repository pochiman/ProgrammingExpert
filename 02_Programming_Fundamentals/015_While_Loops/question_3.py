# Write a program that continually asks the user to enter a word until they enter the word "q" or "quit", at which 
# point the program should print the average length of all of the entered words, excluding the "q" or "quit".

# If the user doesn't enter any words (i.e., immediately enters "q" or "quit"), your program shouldn't print anything.

# You'll have to use the following strings:
# 1) "Enter a word: "
# 2) "The average word length is: _."

##### Solution 1 #####

# word_length_sum = 0
# word_count = 0

# while True:
#     word = input("Enter a word: ")

#     if word == "q" or word == "quit":
#         break

#     word_length_sum += len(word)
#     word_count += 1

# if word_count > 0:
#     average_word_length = word_length_sum / word_count
#     print(f"The average word length is: {average_word_length}.")

##### Solution 2 #####

words = []

while True:
    word = input("Enter a word: ")

    if word == "q" or word == "quit":
        break

    words.append(word)

if len(words) > 0:
    word_length_sum = 0

    for word in words:
        word_length_sum += len(word)

    average_word_length = word_length_sum / len(words)
    print(f"The average word length is: {average_word_length}.")