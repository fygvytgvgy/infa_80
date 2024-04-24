def ing(str):
    if len(str) < 3:
        return str
    if str[-3:] == 'ing':
        return str + 'ly'
    return str + 'ing'

print(ing('abc'))
print(ing('string'))
print(ing('fe'))