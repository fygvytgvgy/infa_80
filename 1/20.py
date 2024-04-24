
def to_uppercase(str):
    num = 0
    for i in str[:4]:
        if i.upper() == i:
            num += 1
    if num >= 2:
        return str.upper()
    return str

print(to_uppercase('Python'))  
print(to_uppercase('PyThon'))  