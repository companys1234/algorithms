n = str(input())
c = 0

i = 0  # Начинаем с первого индекса
while i < len(n):
    if n[i] == '1':
        if i + 2 < len(n) and n[i] == '1' and n[i + 1] == '4' and n[i + 2] == '4':
            c += 3
        elif i + 1 < len(n) and n[i] == '1' and n[i + 1] == '4':
            c += 2
        else:
            c += 1
    i += 1
if c == len(n):
    print('YES')
else:
    print('NO')