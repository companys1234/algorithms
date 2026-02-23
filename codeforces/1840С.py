t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))

    total = 0
    i = 0
    while i < n:
        if a[i] <= q:
            # Начало хорошего отрезка
            j = i
            while j < n and a[j] <= q:
                j += 1
            L = j - i  # длина хорошего отрезка
            if L >= k:
                m = L - k + 1
                total += m * (m + 1) // 2
            i = j  # перепрыгиваем весь хороший отрезок
        else:
            i += 1
    print(total)