t = int(input())
for _ in range(t):
    n = list(map(int,input().split()))
    n = sorted(n)
    for i in range(len(n)-1):
        n[i] *= -1
    print(sum(n))