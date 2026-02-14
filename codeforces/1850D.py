t = int(input())
for _ in range(t):
    max_1 = 0
    z  = []
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a = sorted(a)
    for i in range(n-1):
        if a[i+1] - a[i] <= k:
            z.append(1)
        else:
            z.append(0)
    s  = 0
    for i in z:
        if i == 1:
            s += 1
            if s > max_1:
                max_1 = s
        elif i == 0:
            s = 0

    v = (n - max_1)
    print(v-1)