t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Обрабатываем слева направо
    for i in range(n - 2):
        if a[i] < 0:
            break
        ops = a[i]  # Сколько операций нужно на позиции i+1
        a[i] -= ops
        a[i + 1] -= 2 * ops
        a[i + 2] -= ops

    # Проверяем, все ли элементы стали нулями
    if all(x == 0 for x in a):
        print("YES")
    else:
        print("NO")