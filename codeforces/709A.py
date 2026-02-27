n, b, d = map(int, input().split())
a = list(map(int, input().split()))

c = 0
z = 0

# Один проход: сразу фильтруем и считаем
for x in a:
    if x <= b:  # Фильтруем на лету
        z += x
        if z > d:
            z = 0
            c += 1

print(c)