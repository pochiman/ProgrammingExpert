# Use multiple for loops to iterate through the provided list, string, and tuple, and print all of their elements, each on a separate line.

# First print all of the list items, then all of the string characters, then all of the tuple items.

# Provided List, String, and Tuple
lst = ["tim", "is", "the", "best", "instructor"]
string = "..."
tupl = ("and", "he", "is", "great")

##### Expected Output #####
# tim
# is
# the
# best
# instructor
# .
# .
# .
# and
# he
# is
# great

##### Solution 1 #####
# for item in lst:
#     print(item)

# for character in string:
#     print(character)

# for item in tupl:
#     print(item)

##### Solution 2 #####
for idx in range(len(lst)):
  item = lst[idx]
  print(item)

for idx in range(len(string)):
  character = string[idx]
  print(character)

for idx in range(len(tupl)):
  item = tupl[idx]
  print(item)