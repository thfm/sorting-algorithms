def insert_element(num, array):
    for i, val in reversed(list(enumerate(array))):
        if num > val:
            array.insert(i + 1, num)
            return
    array.insert(0, num)


def insertion_sort(array: list):
    subarray = [array[0]]
    for num in array[1:]:
        insert_element(num, subarray)
    return subarray
