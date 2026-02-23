n, m = map(int, input().split())
a = sorted(map(int, input().split()))

best = 10**10
for i in range(m - n + 1):          # ← все окна длины n
    diff = a[i + n - 1] - a[i]
    best = min(best, diff)

print(best)