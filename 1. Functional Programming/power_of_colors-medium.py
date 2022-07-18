import random


def random_hex_colors():
    return f'#{random.randbytes(3).hex()}'


def random_rbg_colors():
    return random.randrange(255), random.randrange(255), random.randrange(255)


print(random_hex_colors())
print(random_rbg_colors())
