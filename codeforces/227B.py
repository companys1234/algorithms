n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# Создаём словари с позициями (1-based)
pos_forward = {value: idx + 1 for idx, value in enumerate(a)}
pos_backward = {value: idx + 1 for idx, value in enumerate(a[::-1])}

# Считаем суммы позиций
z1 = sum(pos_forward[i] for i in b)
z2 = sum(pos_backward[i] for i in b)

print(z1, z2)