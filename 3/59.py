sample_dict = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6, 7, 8, 9]}
length = sum(len(value) for value in sample_dict.values())
print("Length of dictionary values:", length)
