def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(numbers):
    return all(is_prime(num) for num in numbers)

sample_data = [0, 3, 4, 7, 9]
print("Are all numbers prime?", check_primes(sample_data))
