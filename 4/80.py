def sum_with_limit(a, b):
    result = a + b
    if 15 <= result <= 20:
        return 20
    else:
        return result

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
print("Sum:", sum_with_limit(num1, num2))
