# Write a program that continually asks the user to enter characters until the user enters a previously entered character 
# or more than one character at a time.  After, the program should print the number of unique characters that were entered.

# Use a set to accomplish this.

##### Sample Output 1 #####
# Enter a character: ab
# Number of unique characters entered: 0

##### Sample Output 2 #####
# Enter a character: a
# Enter a character: ab
# Number of unique characters entered: 1

##### Sample Output 3 #####
# Enter a character: a
# Enter a character: b
# Enter a character: c
# Enter a character: b
# Number of unique characters entered: 3

# You'll have to use the strings:
# "Enter a character: "
# "Number of unique characters entered: _"

characters = set()

while True:
    character = input("Enter a character: ")
    if len(character) > 1:
        break

    if character in characters:
        break

    characters.add(character)

print(f"Number of unique characters entered: {len(characters)}")