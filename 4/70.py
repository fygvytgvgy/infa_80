lines = []
while True:
    line = input("Enter a line (blank line to terminate): ")
    if line:
        lines.append(line.lower())
    else:
        break

for line in lines:
    print(line)
