from itertools import islice
from random import randint

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
