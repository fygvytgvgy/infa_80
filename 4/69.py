numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = len([num for num in numbers if num % 2 == 0])
odd_count = len(numbers) - even_count
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
