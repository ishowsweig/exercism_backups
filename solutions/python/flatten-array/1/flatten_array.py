def flatten(iterable, depth=None):
    result = []
    for item in iterable:
        if item is None:
            continue
        elif isinstance(item, list) and depth != 0:
            next_depth = None if depth is None else depth - 1
            result.extend(flatten(item, next_depth))
        else:
            result.append(item)
    return result