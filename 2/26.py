def sort_tuple_list(tuple_list):
    return sorted(tuple_list, key=lambda x: x[-1])

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Sorted list by last element in each tuple:", sort_tuple_list(sample_list))
