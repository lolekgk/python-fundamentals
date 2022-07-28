from random import random

history = []


def random_number():
    global history
    while True:
        number = random()
        history.append(number)
        yield number


# gen = random_number()

# for _ in range(10):
#     num = next(gen)

# print(history)
