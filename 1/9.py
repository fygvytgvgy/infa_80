def remove_char(str, n):
    first = str [:n]
    last = str [n+1:]
    return first + last

print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))