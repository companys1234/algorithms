
n,m = map(int,input().split())
a = list(map(int,input().split()))
target = max(a)
if target <= m:
    print(len(a))
else:
    z = []
    for i in a:
        f = 0
        while i > 0:
            f += 1
            i -= m
        z.append(f)
    tar = max(z)
    s = len(a) - z[::-1].index(tar)
    print(s)