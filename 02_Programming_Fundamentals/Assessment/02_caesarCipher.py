##### Caesar Cipher #####
# Write a function that accepts a string and returns the caesar cipher encoding of that string according to 
# a secondary input parameter named offset.

# The caesar cipher encoding of a string involves shifting each character in the string a set number of 
# positions previous in the alphabet.  For example, if you were performing a caesar cipher of the string 
# "tim" with offset = 2 you would get "rgk".  "t" is shifted two positions to "r", "i" is shifted two 
# positions to "g" and "m" is shifted two positions to "k".

# In the situation where the shift of a character results in it being a position before "a", the positions wrap 
# and the next character should be "z".  For example, the caesar cipher of "ab" with offset = 2 would be "yz". 

# offset will always be a positive integer that is no greater than 26 and the input string will only contain 
# lowercase letters.

##### Sample Input 1 #####
# string = "hello"
# offset = 3

##### Sample Output 1 #####
# "ebiil"

##### Sample Input 2 #####
# string = "apple"
# offset = 5

##### Sample Output #####
# "vkkgz"

def caesar_cipher(string, offset):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    encoded_string = ''

    for character in string:
        position = alphabet.index(character)
        offset_position = position - offset
        # No need to handle negative positions because of negative indexing
        encoded_character = alphabet[offset_position]
        encoded_string += encoded_character

    return encoded_string