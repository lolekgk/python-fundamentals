import random


def random_hex_colors():
    return f'#{random.randbytes(3).hex()}'


def random_rbg_colors():
    pass


print(random_hex_colors())
