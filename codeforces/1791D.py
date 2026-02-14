t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    # suffix_unique[i] = число уникальных символов в s[i:]
    suffix_unique = [0] * (n + 1)
    seen = set()
    for i in range(n - 1, -1, -1):
        seen.add(s[i])
        suffix_unique[i] = len(seen)

    left_seen = set()
    best = 0
    # Разрез после i-го символа: a = s[0:i], b = s[i:n], где i от 1 до n-1
    for i in range(n - 1):  # i от 0 до n-2 → разрез между i и i+1
        left_seen.add(s[i])
        total = len(left_seen) + suffix_unique[i + 1]
        if total > best:
            best = total
    print(best)