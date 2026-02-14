t = int(input())
for _ in range(t):
    n = int(input())

    a = 0
    while n % 2 == 0:
        n //= 2
        a += 1

    b = 0
    while n % 3 == 0:
        n //= 3
        b += 1

    if n != 1 or a > b:
        print(-1)
    else:
        print(2 * b - a)
