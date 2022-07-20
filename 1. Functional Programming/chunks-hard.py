import math
from itertools import combinations_with_replacement, islice
from random import choice, randint

alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]


def to_chunks(data, min_chunk=4, max_chunk=7):
    chunks_lengths = []
    while sum(chunks_lengths) != len(data):
        chunks_lengths.append(randint(min_chunk, max_chunk))
        if sum(chunks_lengths) > len(data):
            chunks_lengths.clear()

    it = iter(data)
    return [list(islice(it, elem)) for elem in chunks_lengths]


chunks = to_chunks(alphabet)
print(chunks)


def to_chunks2(data, min_=4, max_=7):
    max_chunk_length = int(len(data) / min_)
    min_chunk_length = math.ceil(len(data) / max_)
    chunks_lengths = [
        el
        for el in combinations_with_replacement(
            range(min_, max_ + 1),
            randint(min_chunk_length, max_chunk_length),
        )
        if sum(el) == 24
    ]
    it = iter(data)
    return [list(islice(it, item)) for item in choice(chunks_lengths)]


chunks2 = to_chunks2(alphabet)
print(chunks2)
