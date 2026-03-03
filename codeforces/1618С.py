from math import gcd
from functools import reduce


def gcd_list(numbers):
    if not numbers:
        return 0
    return reduce(gcd, numbers)


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # Вариант 1: нечётные индексы (0,2,4...) делятся на d
    z1 = [a[i] for i in range(0, n, 2)]  # индексы 0, 2, 4...
    z2 = [a[i] for i in range(1, n, 2)]  # индексы 1, 3, 5...

    d1 = gcd_list(z1)

    # Проверяем вариант 1
    if d1 > 1:
        ok = True
        for z in z2:
            if z % d1 == 0:
                ok = False
                break
        if ok:
            print(d1)
            return

    # Вариант 2: чётные индексы (1,3,5...) делятся на d
    d2 = gcd_list(z2)

    # Проверяем вариант 2
    if d2 > 1:
        ok = True
        for z in z1:
            if z % d2 == 0:
                ok = False
                break
        if ok:
            print(d2)
            return

    # Ни один вариант не подошёл
    print(0)


# Основная программа
t = int(input())
for _ in range(t):
    solve()