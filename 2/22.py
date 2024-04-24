def multiply_list(items):
    result = 1
    for x in items:
        result *= x
    return result

sample_list = [1, 2, 3, 4, 5]
print("Product of all items in the list:", multiply_list(sample_list))
