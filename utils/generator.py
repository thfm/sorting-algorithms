import random

def gen_random_array(size, minimum=-1000, maximum=1000):
    array = []
    for _ in range(size):
        array.append(random.randint(minimum, maximum))
    return array
