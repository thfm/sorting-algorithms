from utils.shared import swap_elements
from utils.validator import is_sorted
from copy import deepcopy


def bubble_sort(array):
    # A copy of the original array is made, so that any modifications
    # do not affect it
    working_arr = deepcopy(array)
    while not is_sorted(working_arr):
        for i in range(len(working_arr) - 1):
            if working_arr[i] > working_arr[i + 1]:
                swap_elements(working_arr, i, i + 1)
    return working_arr
