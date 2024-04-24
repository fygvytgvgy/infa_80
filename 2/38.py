from itertools import permutations

def generate_permutations(input_list):
    return list(permutations(input_list))

sample_list = [1, 2, 3]
print("All permutations of the list:", generate_permutations(sample_list))
