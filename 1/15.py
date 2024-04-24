def add_tags(tag, str):
    return "<%s>%s</%s>" % (tag, str, tag)

print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))