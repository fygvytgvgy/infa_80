input = input("Your input: ")

words = [word for word in input.split(',')]

print(",".join(sorted(list(set(words)))))