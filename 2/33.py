array_3d = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
for row in array_3d:
    for sub_row in row:
        print(' '.join(sub_row))
    print()
