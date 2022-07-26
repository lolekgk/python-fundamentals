def paginate(items, max_elements, page_number):
    page_start = (page_number - 1) * max_elements
    page_end = page_start + max_elements
    return items[page_start:page_end]
