def char_exch(str):
    str = str[-1:] + str[1:-1] + str[:1]
    return str
print(char_exch('abcd'))