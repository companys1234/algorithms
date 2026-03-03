n = int(input())

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

count = 1  # Количество копий каждого человека в текущем раунде (1, 2, 4, 8...)

# Находим, в каком раунде находится n-ая баночка
while n > 5 * count:
    n -= 5 * count  # Вычитаем все баночки текущего раунда
    count *= 2      # В следующем раунде копий в 2 раза больше

# Определяем, какой человек пьёт эту баночку
person_index = (n - 1) // count
print(names[person_index])