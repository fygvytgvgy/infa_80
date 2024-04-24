sample_dict = {'a': 10, 'b': 20, 'c': 30}
keys_to_check = ['a', 'b']
if all(key in sample_dict for key in keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
