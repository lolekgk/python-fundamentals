from random import random

history = []


def random_number():
    while True:
        yield random()


gen = random_number()

for _ in range(10):
    num = next(gen)
    print(num)
    history.append(num)

print(history)
