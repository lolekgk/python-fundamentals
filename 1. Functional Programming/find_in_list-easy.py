from collections import namedtuple


def find_item(data, key):
    Result = namedtuple('Result', ['value', 'index'])
    results_list = [
        Result(item, i) for i, item in enumerate(data) if str(key) in str(item)
    ]
    return results_list if results_list else ()


result = find_item(['nine', 'ten', 'eleven', 'twelve'], 'el')
print(result)
