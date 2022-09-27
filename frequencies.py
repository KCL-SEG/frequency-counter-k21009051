"""Frequencies function."""

def frequencies(items):
    frequencies = {}

    # Convert every element in the list to a string
    for element in items:
        index = items.index(element)
        items[index] = str(element)
    
    # Generate a unique set of the elements to be counted
    set_items = set(items)

    for element in set_items:
        count = items.count(element)
        frequencies[element] = count

    return frequencies
