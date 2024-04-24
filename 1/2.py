string = 'google.com'

def count_freq(str):
    dict = {}
    for i in str:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)

count_freq(string)