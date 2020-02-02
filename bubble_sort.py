from utils import swap_elements
from validator import is_sorted

def bubble_sort(array):
    while not is_sorted(array):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap_elements(array, i, i + 1)
