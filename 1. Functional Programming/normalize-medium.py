import math
import random
import statistics
from pprint import pprint

data = [random.randint(0, 100000) for x in range(100)]


def random_number(data):
    """Normalizes given list of integers to range <0, 1>"""
    smallest_num, biggest_num = min(data), max(data)
    return (
        (num - smallest_num) / (biggest_num - smallest_num) for num in data
    )


# https://stats.stackexchange.com/questions/380276/how-to-normalize-data-between-0-and-1
def normalize_data(data):
    """Normalizes given list of integers to range <0, 1)"""
    standard_score_data = [
        (num - statistics.mean(data)) / statistics.stdev(data) for num in data
    ]
    return (1 / (1 + math.exp(-num)) for num in standard_score_data)


pprint(list(random_number(data)))


a = list(normalize_data(data))
