sample_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 20}
result = {}
for key, value in sample_dict.items():
    if value not in result.values():
        result[key] = value
print("Dictionary after removing duplicates:", result)
