# -*- coding: utf-8 -*-
"""1335С

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-6ZHeZ31qXEC3tYwp4OcKykDuL4oXdg5
"""

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Создаем словарь частот
    count_dict = {}
    for num in a:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Если нужно просто вывести частоты чисел
    print(count_dict.values())

    # Находим максимальную частоту
    if count_dict:  # Проверяем, что словарь не пустой
        max_freq = max(count_dict.values())
    else:
        max_freq = 0

    # Ваша логика для вычисления c (непонятна из кода)
    c = 0
    for i in range(1, max_freq + 1):
        # Непонятное условие - возможно, вы хотели что-то другое?
        if i > c and i == (max_freq - i):
            c = i

    print(c+1)