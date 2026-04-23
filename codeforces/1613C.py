import sys


# Ускоряем чтение входных данных
def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    ans_list = []

    for _ in range(t):
        n = int(next(it))
        h = int(next(it))
        a = [int(next(it)) for _ in range(n)]

        # Бинарный поиск по ответу k
        l, r = 1, h
        best_k = h

        while l <= r:
            k = (l + r) // 2

            # Считаем суммарный урон для текущего k
            damage = k  # Последний удар всегда наносит k урона
            for i in range(n - 1):
                damage += min(k, a[i + 1] - a[i])
                # Небольшая оптимизация: если уже набрали нужный урон,
                # дальнейшее суммирование не нужно
                if damage >= h:
                    break

            # Если урона достаточно, пробуем уменьшить k (ищем минимальный)
            if damage >= h:
                best_k = k
                r = k - 1
            else:
                l = k + 1

        ans_list.append(str(best_k))

    print('\n'.join(ans_list))


solve()