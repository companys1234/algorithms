t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Инициализируем максимум первым элементом (на случай если все отрицательные)
    max_sum = -float('inf')
    current_sum = 0

    for i in range(n):
        if i == 0:
            # Первый элемент всегда начинает новый подотрезок
            current_sum = a[i]
        else:
            # Проверяем чётность текущего и предыдущего
            if a[i] % 2 != a[i - 1] % 2:
                # Чётности разные: можно продолжить или начать заново
                current_sum = max(a[i], current_sum + a[i])
            else:
                # Чётности одинаковые: разрываем цепочку, начинаем с текущего
                current_sum = a[i]

        # Обновляем глобальный максимум
        if current_sum > max_sum:
            max_sum = current_sum

    print(max_sum)