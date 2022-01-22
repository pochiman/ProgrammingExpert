# Write a program that asks the user to enter a string and prints the string's characters 
# and their frequencies in any order and in the following format: key: frequency.

# You'll have to use the string: "Enter a string: "

##### Solution 1 #####
# string = input("Enter a string: ")

# character_frequencies = {}

# for character in string:
#     if character not in character_frequencies:
#         character_frequencies[character] = 0

#     character_frequencies[character] += 1

# for key in character_frequencies:
#     frequency = character_frequencies[key]

#     print(f"{key}: {frequency}")

##### Solution 2 #####
string = input("Enter a string: ")

character_frequencies = {}

for character in string:
    character_frequencies[character] = character_frequencies.get(character, 0) + 1

for key in character_frequencies:
    frequency = character_frequencies[key]

    print(f"{key}: {frequency}")