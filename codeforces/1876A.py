t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Создаём пары (стоимость передачи, вместимость) и сортируем по стоимости
    villagers = sorted(zip(b, a))

    cost = 0
    notified = 0  # Сколько уже оповещено

    for b_i, a_i in villagers:
        if notified >= n:
            break

        # Первого человека всегда оповещаем напрямую
        if notified == 0:
            cost += p
            notified += 1

        # Если осталось кого оповещать
        if notified < n:
            if b_i < p:
                # Выгоднее использовать этого жителя как передатчика
                can_notify = min(a_i, n - notified)
                cost += can_notify * b_i
                notified += can_notify
            else:
                # Выгоднее оповестить остальных напрямую
                remaining = n - notified
                cost += remaining * p
                notified = n

    print(cost)