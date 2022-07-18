def paginate(items, max_elements, page_number):
    paginated_items = [items[i:i+max_elements] for i in range(0, len(items), max_elements)]
    return paginated_items[page_number - 1] # lists start indexing from 0
    
    
print(paginate(list(range(101)), 10, 5))

# We can also use zip_longest from itertools, but it'll fill rest of page with fillvalue