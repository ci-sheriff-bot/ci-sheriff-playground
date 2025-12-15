def count_unique_items(items):
    # BUG: off-by-one
    return len(set(items)) + 1
