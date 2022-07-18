def paginate(items, max_elements, page_number):
    if is_valid_page(page_number):
        paginated_items = [items[i:i+max_elements] for i in range(0, len(items), max_elements)]
        return paginated_items[page_number - 1] # lists start indexing from 0


def is_valid_page(page_number):
    if page_number < 1:
        raise TypeError('Page number must be positive.')
    return True


print(paginate(list(range(101)), 10, 0))

# We can also use zip_longest from itertools, but it'll fill rest of page with fillvalue
# Or more-itertools library -> chunked method
