def longer_than_n(words, n):
    return [word for word in words if len(word) > n]

sample_list = ['apple', 'banana', 'orange', 'grape', 'kiwi']
n = 5
print("Words longer than", n, "characters:", longer_than_n(sample_list, n))
