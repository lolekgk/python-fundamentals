def paginate(items, max_elements, page_number):
    if is_valid_page(page_number):
        page_start = (page_number - 1) * max_elements
        page_end = page_start + max_elements
        return items[page_start:page_end]


def is_valid_page(page_number):
    if not isinstance(page_number, int):
        raise TypeError('Page number must be an int type.')
    elif page_number < 1:
        raise ValueError('Page number must be positive.')
    return True
