import random

data = [random.randint(0, 100000) for x in range(100)]


def random_number(data):
    """Normalizes given list of integers to range <0, 1>"""
    smallest_num, biggest_num = min(data), max(data)
    return [
        (num - smallest_num) / (biggest_num - smallest_num) for num in data
    ]


# https://stats.stackexchange.com/questions/380276/how-to-normalize-data-between-0-and-1
def normalize_data(data):
    """Normalizes given list of integers to range <0, 1)"""
    epsilon = 0.01
    return [
        (epsilon + (1 - 2 * epsilon))
        * (num - min(data))
        / (max(data) - min(data))
        for num in data
    ]
