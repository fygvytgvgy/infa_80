sample_dict = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6, 7, 8, 9]}
count = sum(isinstance(value, list) for value in sample_dict.values())
print("Number of items in dictionary values that are lists:", count)
