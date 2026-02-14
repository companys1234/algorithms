t = int(input())
for _ in range(t):
    n = int(input())
    k = n // 2020
    remainder = n % 2020
    if remainder <= k:
        print("YES")
    else:
        print("NO")
