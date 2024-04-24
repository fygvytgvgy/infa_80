
def not_poor(str):
    not1 = str.find('not')
    poor1 = str.find('poor')
    if poor1 > not1 and poor1 > 0 and not1 > 0: 
        str = str.replace(str[not1:(poor1+4)],'good')
        return str
    else:
        return str

print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))