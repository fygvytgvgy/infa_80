
def insert_string_middle(word, str):
    return word[:len(word)//2] + str + word[len(word)//2:]

print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))    
print(insert_string_middle('<<>>', 'HTML'))