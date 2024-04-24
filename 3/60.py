def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0

sample_dict = {'a': {'b': {'c': 1}}}
depth = dict_depth(sample_dict)
print("Depth of the dictionary:", depth)
