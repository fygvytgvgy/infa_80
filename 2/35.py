import random

def shuffle_list(input_list):
    shuffled_list = input_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list

sample_list = [1, 2, 3, 4, 5]
print("Shuffled list:", shuffle_list(sample_list))
