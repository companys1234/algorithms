import math

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    i = math.ceil(n / k)

    s = i * k
    print(math.ceil(s / n))