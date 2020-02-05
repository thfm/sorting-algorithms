# Places a given number into its correct (sorted) position in an array
def insert_element(num, array):
    # Quick edge case for optimisation
    if num < min(array):
        array.insert(0, num)
    # Loops through the list in reverse order
    for i, val in reversed(list(enumerate(array))):
        if num > val:
            array.insert(i + 1, num)
            return


def insertion_sort(array: list):
    subarray = [array[0]] # Stores all sorted items
    for num in array[1:]:
        insert_element(num, subarray)
    return subarray
