t = int(input())
for _ in range(t):
    a,b,n = map(int,input().split())
    x = list(map(int,input().split()))
    x = sorted(x)
    c = 0
    for i in x:
        c += (min(a-1,i))
    print(c+b)