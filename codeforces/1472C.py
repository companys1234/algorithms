t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Создаем массив для хранения результатов, начиная с позиций
    dp = [0] * (n + 1)
    max_result = 0

    # Идем с конца массива к началу
    for i in range(n - 1, -1, -1):
        next_pos = i + a[i]  # Куда мы попадем из текущей позиции
        if next_pos < n:
            dp[i] = a[i] + dp[next_pos]
        else:
            dp[i] = a[i]

        # Обновляем максимальный результат
        if dp[i] > max_result:
            max_result = dp[i]

    print(max_result)