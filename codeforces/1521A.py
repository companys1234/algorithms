idx = 0
t = int(input())
idx += 1
results = []

for _ in range(t):
    A, B = map(int, input().split())
    idx += 2

    if B == 1:
        results.append("NO")
    else:
        x = A
        y = A * B
        z = A * (B + 1)
        results.append("YES")
        results.append(f"{x} {y} {z}")

print("\n".join(results))
