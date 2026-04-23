import sys

# Увеличиваем скорость ввода для больших данных
input = sys.stdin.readline


def solve():
    try:
        n_line = input()
        if not n_line:
            return
        n = int(n_line)
        z = list(map(int, input().split()))
    except ValueError:
        return

    # Проверка префиксных сумм: pre[0]...pre[n-2] (индексы 0..n-2 в массиве префиксов соответствуют длинам 1..n-1)
    # Pre[i] = sum(z[0..i])

    current_sum = 0
    prefix_ok = True
    for i in range(n - 1):  # Проверяем префиксы длиной от 1 до n-1
        current_sum += z[i]
        if current_sum <= 0:
            prefix_ok = False
            break

    if not prefix_ok:
        print("NO")
        return

    # Проверка суффиксных сумм: suf[n-1]...suf[1] (индексы в массиве)
    # Суффикс, начинающийся с индекса i (0-indexed), это sum(z[i..n-1])
    # Нам нужны суффиксы, которые остаются, если Адель берет префикс.
    # Адель не может взять [0, n-1].
    # Если Адель берет [0, r], остаток - суффикс starting at r+1.
    # r может быть от 0 до n-2. Значит начало суффикса от 1 до n-1.
    # То есть нам нужны суммы z[1..n-1], z[2..n-1], ..., z[n-1..n-1].

    current_sum = 0
    suffix_ok = True
    for i in range(n - 1, 0, -1):  # Идем с конца к началу, индексы n-1 down to 1
        current_sum += z[i]
        if current_sum <= 0:
            suffix_ok = False
            break

    if suffix_ok:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    solve()