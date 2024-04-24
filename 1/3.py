

def get_str(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]

print(get_str('w3resource'))
print(get_str('w3'))
print(get_str('w'))