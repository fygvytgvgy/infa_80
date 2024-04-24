def sum_list(items):
    total = 0
    for x in items:
        total += x
    return total

sample_list = [1, 2, 3, 4, 5]
print("Sum of all items in the list:", sum_list(sample_list))
