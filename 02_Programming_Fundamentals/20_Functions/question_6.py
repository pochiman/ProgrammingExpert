# Write the function running_sums(numbers), which takes in a list of integers and returns a new list of the same length as numbers, 
# where the element at index i in the new list is equal to numbers[0] + numbers[1] + ... + numbers[i - 1] + numbers[i].
# You can assume that numbers will only contain integers.

##### Sample Output #####
# >>> sums = running_sums([5, 4, 2, 1, 5, 6, 4])
# >>> print(sums)
# [5, 9, 11, 12, 17, 23, 27]

def running_sums(numbers):
    sums = []

    current_sum = 0
    for number in numbers:
        current_sum += number
        sums.append(current_sum)

    return sums