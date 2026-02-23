n,m = map(int,input().split())

d = True
if m % n != 0:
    print(-1)
    d = False
if d:
    c = 0
    z = n
    x = 0
    y = 0
    d = int(m/n)
    d1 = d
    d2 = d
    while d % 2 == 0:
        x += 1
        d /= 2
    while d % 3 == 0:
        y += 1
        d /= 3
    if int(d) != 1:
        print(-1)
    else:
        print(x+y)