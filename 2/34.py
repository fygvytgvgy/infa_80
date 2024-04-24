def remove_even_numbers(input_list):
    return [number for number in input_list if number % 2 != 0]

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List after removing even numbers:", remove_even_numbers(sample_list))
