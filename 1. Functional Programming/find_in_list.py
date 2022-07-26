from collections import namedtuple


def find_item(data, key):
    Item = namedtuple('Result', ['value', 'index'])
    items_list = [
        Item(item, i) for i, item in enumerate(data) if str(key) in str(item)
    ]
    return items_list if items_list else ()


result = find_item(['nine', 'ten', 'eleven', 'twelve'], 'el')
print(result)
