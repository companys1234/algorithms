t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    res = []
    idx = -1

    # Ищем первый район, у которого банда отличается от банды первого района
    for i in range(1, n):
        if a[i] != a[0]:
            idx = i
            res.append((1, i + 1))  # соединяем 1-й район с i+1-м

    # Если все банды одинаковые
    if idx == -1:
        print("NO")
        continue

    # Соединяем все оставшиеся районы с той же бандой, что и первый,
    # с найденным ранее отличным районом
    for i in range(1, n):
        if a[i] == a[0]:
            res.append((idx + 1, i + 1))

    print("YES")
    for x, y in res:
        print(x, y)
