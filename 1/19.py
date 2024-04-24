def reverse_str(str):
    if len(str) % 4 == 0:
        return ''.join(reversed(str))
    return str

print(reverse_str('abcd'))
print(reverse_str('Python'))