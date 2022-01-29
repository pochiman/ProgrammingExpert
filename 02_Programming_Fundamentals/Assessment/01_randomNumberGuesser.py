##### Random Number Guesser #####
# Write a program that asks the user to enter two integers representing the start and the end of a range.
# The program should then generate a random number within this range (inclusively) and ask the user to
# guess numbers until they guess the randomly generated number.  Once the user guesses the random
# number, the program should tell them how many attempts it took them to guess it.

# Your program needs to ensure that the range of numbers given is valid.  For example, if the user enters a 
# number for the end of the range that is less than the start of the range your program needs, ask them to 
# enter a valid number.  Your program must also handle any other errors that might occur, like the user 
# entering a string instead of an integer.

# Note: You may assume the start of the range will never be negative (i.e you don't need to handle 
# negative values).

# Your program must use the same prompts and output as shown in the sample output below.
# Make sure to use `random.randint` to pick your random number.

##### Sample Output 1 #####
# Enter the start of the range: 1
# Enter the end of the range: 5
# Guess a number: 2
# Guess a number: 3
# You guessed the number in 2 attempts

##### Sample Output 2 #####
# Enter the start of the range: 5
# Enter the end of the range: 4
# Please enter a valid number.
# Enter the end of the range: 7
# Guess a number: 6
# You guess the number in 1 attempt

##### Sample Output 3 #####
# Enter the start of the range: hello
# Please enter a valid number.
# Enter the start of the range: 8
# Enter the end of the range: 4
# Please enter a valid number.
# Enter the end of the range: 20
# Guess a number: 6
# Guess a number: 7
# Guess a number: hello
# Please enter a valid number.
# Guess a number: 9
# You guessed the number in 3 attempts

import random

start = input('Enter the start of the range: ')
while not start.isdigit():
    print('Please enter a valid number.')
    start = input('Enter the start of the range: ')

end = input('Enter the end of the range: ')
while not end.isdigit() or int(end) < int(start):
    print('Please enter a valid number.')
    end = input('Enter the end of the range: ')

random_number = random.randint(int(start), int(end))

guess = None
attempts = 0

while guess != random_number:
    guessed_number = input("Guess a number: ")
    if not guessed_number.isdigit():
        print("Please enter a valid number.")
        continue
    
    attempts += 1
    guess = int(guessed_number)

suffix = ""
if attempts > 1:
    suffix = "s"

print(f'You guessed the number in {attempts} attempt{suffix}')