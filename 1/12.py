sentence = 'the quick brown fox jumps over the lazy dog'

def count_occurr(str):
    dict = {}
    words = str.split()
    for i in words:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(count_occurr(sentence))