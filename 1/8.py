list = ['PHP', 'Exercise', 'Backend']

def longest_one(list):
    count = 0
    for i in list:
        if len(i) > count:
            count = len(i)
            word = i
    return word, count

print(longest_one(list))