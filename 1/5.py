a = 'abc'
b = 'xyz'

def sep_str(a, b):
    a1 = b[:2] + a[2:]
    b1 = a[:2] + b[2:]
    print(f'{a1} {b1}')

sep_str(a, b)