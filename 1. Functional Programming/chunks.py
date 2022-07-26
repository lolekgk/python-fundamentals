from random import randint

alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]


def to_chunks(data, min_=4, max_=7):
    if len(data) <= max_:
        return [data]
    elif len(data) <= max_ * 2:
        if len(data) > min_ + max_:
            chunk_length = randint(len(data) - max_, max_)
        else:
            chunk_length = randint(min_, len(data) - min_)
        return [data[:chunk_length], data[chunk_length:]]
    else:
        chunk_length = randint(min_, max_)
        divided_data = [data[:chunk_length]]
        divided_data.extend(to_chunks(data[chunk_length:], min_, max_))
        return divided_data
