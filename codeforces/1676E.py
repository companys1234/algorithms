import sys
from bisect import bisect_left

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    # Сортируем по убыванию (берём самые сладкие сначала)
    a.sort(reverse=True)

    # Префиксные суммы
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]

    # Обработка запросов
    for _ in range(q):
        x = int(input())

        # Если даже все конфеты не дают нужное количество сахара
        if prefix[n] < x:
            print(-1)
        else:
            # Бинарный поиск минимального k, где prefix[k] >= x
            k = bisect_left(prefix, x)
            print(k)