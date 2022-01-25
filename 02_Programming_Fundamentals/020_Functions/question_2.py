# Write the function find_all_odds(lst), which takes in a list of integers and returns a new list containing all of the 
# odd numbers of the original list, in the order in which they appear.  You can assume that lst will only contain integers.

def find_all_odds(lst):
    odds_list = []

    for element in lst:
        if element % 2 == 1:
            odds_list.append(element)

    return odds_list