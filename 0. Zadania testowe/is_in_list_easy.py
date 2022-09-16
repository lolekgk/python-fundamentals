def is_in_list(list_, element_to_find):
    """Check wheater element is in list without in operator"""
    if list_.count(element_to_find) > 0:
        return True
    return False
