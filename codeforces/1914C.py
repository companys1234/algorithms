t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = 0
    max_b = 0
    ans = 0

    # Перебираем, сколько квестов открываем
    for i in range(min(n, k)):
        c += a[i]
        max_b = max(max_b, b[i])
        remaining = k - (i + 1)
        current_total = c + max_b * remaining
        ans = max(ans, current_total)

    print(ans)
