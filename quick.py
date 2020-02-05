from random import randint
from insertion import insertion_sort


def quick_sort(array):
    # If the array has one or zero elements, it is already sorted
    if len(array) <= 1:
        return array
    elif len(array) < 5:
        # Uses insertion sort on short arrays, for efficiency
        return insertion_sort(array)

    partition = array[randint(0, len(array) - 1)]
    left = []
    right = []
    for num in array:
        if num < partition:
            left.append(num)
        else:
            right.append(num)
    left = quick_sort(left)
    right = quick_sort(right)
    return left + right
