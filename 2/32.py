def remove_elements(input_list):
    indices_to_remove = [0, 4, 5]
    return [element for index, element in enumerate(input_list) if index not in indices_to_remove]

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("List after removing specified elements:", remove_elements(sample_list))
