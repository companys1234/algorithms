import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = ''
    c_max = 0
    z = 0
    z2 = 0
    for i in range(n):
        k = str(input())
        if k.count('#') > c_max:
            z = i + 1
            s = k
            c_max = k.count('#')

    med = math.ceil(c_max / 2)
    h = 0
    for i in s:
        z2 += 1
        if i == '#':
            h += 1
        if h == med:
            print(z, z2)
            break