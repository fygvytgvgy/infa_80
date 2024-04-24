def remove_odd(str):
    str1 = ''
    for i in range(len(str)):
        if i%2==0:
            str1 = str1 + str[i]
    return str1

print(remove_odd('abcdef'))