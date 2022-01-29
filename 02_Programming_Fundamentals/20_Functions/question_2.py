# Write the function find_all_odds(lst), which takes in a list of integers and returns a new list containing all of the 
# odd numbers of the original list, in the order in which they appear.  You can assume that lst will only contain integers.

##### Sample Output #####
# >>> find_all_odds([1, 2, 3, 4, 5, 6, 5, 5, 3, 2])
# [1, 3, 5, 5, 5, 3]

def find_all_odds(lst):
    odds_list = []

    for element in lst:
        if element % 2 == 1:
            odds_list.append(element)

    return odds_list