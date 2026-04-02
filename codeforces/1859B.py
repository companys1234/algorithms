# Читаем количество тестов
t = int(input())

for _ in range(t):
    # Читаем количество массивов
    n = int(input())

    sum_second_mins = 0
    min_second_min = float('inf')
    global_min = float('inf')

    for _ in range(n):
        # Читаем размер текущего массива
        m = int(input())
        # Читаем элементы массива
        arr = list(map(int, input().split()))

        # Находим два наименьших числа в текущем массиве
        min1 = float('inf')
        min2 = float('inf')

        for x in arr:
            # Обновляем глобальный минимум среди всех чисел
            if x < global_min:
                global_min = x

            # Обновляем два минимума для текущего массива
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x

        # Суммируем вторые минимумы всех массивов
        sum_second_mins += min2

        # Ищем массив, у которого второй минимум наименьший
        if min2 < min_second_min:
            min_second_min = min2

    # Формула результата:
    # (Сумма всех вторых минимумов) - (Наименьший из вторых минимумов) + (Глобальный минимум)
    result = sum_second_mins - min_second_min + global_min
    print(result)