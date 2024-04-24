def insert_end(str):
    if len(str) >= 2:
        str1 = str[-2:]
        return str1 * 4
    else:
        return str

print(insert_end('Python'))
print(insert_end('Exercise'))
print(insert_end('Xd'))
print(insert_end('X'))