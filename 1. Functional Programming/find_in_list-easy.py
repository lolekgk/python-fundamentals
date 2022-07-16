from collections import namedtuple


def find_item(list_of_items, key):
    FoundItem = namedtuple('Result', ['value', 'index'])
    for i, item in enumerate(list_of_items):
        if key in item:
            return FoundItem(item, i)
    return ()


result = find_item(['nine', 'ten', 'eleven'], 'el')
print(result)
