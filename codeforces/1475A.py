t = int(input())
for _ in range(t):
    n = int(input())
    # Это эквивалентно: "n НЕ является степенью двойки"

    if n & (n - 1) == 0:
        # Это степень двойки (включая n=1)
        print('NO')
    else:
        print('YES')