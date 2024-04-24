string = 'restart'

def change_char(str):
    first_char = str[0]
    str = str.replace(first_char, '$')
    str = first_char + str[1:]
    return str

print(change_char(string))