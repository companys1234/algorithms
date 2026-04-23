t = int(input())
for _ in range(t):
    p = int(input())
    p2 = [i for i in range(1,(p*3)+1)]
    z = []
    p3 = sorted(p2,reverse=True)

    l = 0
    for i in range(0,len(p2)-p,2):
        l -= 1
        z.extend([p3[i], p3[i + 1], p3[l]])
    print(*z)
