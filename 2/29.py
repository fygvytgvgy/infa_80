def clone_list(input_list):
    return input_list[:]

sample_list = [1, 2, 3, 4, 5]
cloned_list = clone_list(sample_list)
print("Original list:", sample_list)
print("Cloned list:", cloned_list)
