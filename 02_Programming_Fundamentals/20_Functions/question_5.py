# Write the function trim_list(lst, elements_to_trim), which takes in a list and returns a new version 
# of the input list where the last elements_to_trim elements have been removed.  You can assume that
# elements_to_trim will always be a positive integer that's smaller than the length of lst.

##### Solution 1 #####
# def trim_list(lst, elements_to_trim):
#     trimmed_list = []

#     for idx in range(len(lst) - elements_to_trim):
#         element = lst[idx]
#         trimmed_list.append(element)

#     return trimmed_list

##### Solution 2 #####
def trim_list(lst, elements_to_trim):
    return lst[:len(lst) - elements_to_trim]