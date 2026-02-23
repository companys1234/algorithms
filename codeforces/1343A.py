t = int(input())
for _ in range(t):
    n = int(input())

    def solve(n):
        for k in range(2, 30):  # 2^30 - 1 > 10^9
            divisor = (1 << k) - 1  # 2^k - 1
            if n % divisor == 0:
                return n // divisor
        return -1  # не найдено
    print(solve(n))