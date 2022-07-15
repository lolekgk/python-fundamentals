def is_in_list(list, element_to_find):
    """Check wheater element is in list without in operator"""
    if list.count(element_to_find) > 0:
        return True
    return False


# Test
print(is_in_list([1, 2], 3))
