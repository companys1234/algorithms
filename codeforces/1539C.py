n, k, x = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)

b = 1  # Изначально одна группа
gaps = []  # Список стоимостей для заполнения разрывов

for i in range(len(a) - 1):
    diff = a[i+1] - a[i]
    if diff > x:
        b += 1  # Этот разрыв создает новую группу
        needed = (diff - 1) // x  # Сколько учеников нужно для заполнения
        gaps.append(needed)

# Сортируем разрывы по стоимости (жадный подход)
gaps.sort()

# Заполняем самые дешевые разрывы
for needed in gaps:
    if k >= needed:
        k -= needed
        b -= 1  # Объединили две группы
    else:
        break

print(b)