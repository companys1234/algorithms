t = int(input())
for _ in range(t):
    n, k = input().split()
    a = str(input())
    a = (a * 2)
    a3 = 0
    z = 1
    u = False
    for i in a:
        if i == k:
            u = True
        if u == True and i != 'g':
            z += 1
        if i == 'g':
            u = False
            if z > a3:
                a3 = z
            z = 1
    print(a3 - 1)
