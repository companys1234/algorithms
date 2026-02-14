import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, q = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    # Префиксная сумма: pref[0] = 0, pref[i] = a[0] + ... + a[i-1]
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]

    total_sum = pref[n]

    for _ in range(q):
        l, r, k = map(int, sys.stdin.readline().split())
        seg_len = r - l + 1
        old_seg_sum = pref[r] - pref[l - 1]
        new_total = total_sum - old_seg_sum + k * seg_len

        if new_total % 2 == 1:
            print("YES")
        else:
            print("NO")