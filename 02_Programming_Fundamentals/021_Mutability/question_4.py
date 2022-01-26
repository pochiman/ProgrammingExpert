# Write a function named replace that takes in three parameters: 
# lst (a list of strings), target (a string), and swap_value (another string).

# Your function should replace all instances of target in lst with swap_value, and it 
# shouldn't return anything; in other words, your function should mutate the input list.

def replace(lst, target, swap_value):
    for idx in range(len(lst)):
        element = lst[idx]

        if element == target:
            lst[idx] = swap_value