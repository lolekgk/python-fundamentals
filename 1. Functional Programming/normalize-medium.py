import random

data = [random.randint(0, 100000) for x in range(100)]


def random_number(data):
    smallest_num, biggest_num = min(data), max(data)
    return (
        (num - smallest_num) / (biggest_num - smallest_num) for num in data
    )


print(list(random_number(data)))
