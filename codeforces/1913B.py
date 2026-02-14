import sys


def solve():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    out_lines = []
    index = 1
    for _ in range(t):
        s = data[index].strip()
        index += 1
        n = len(s)
        cnt0 = s.count('0')
        cnt1 = n - cnt0

        # prefix count of zeros
        pref0 = 0
        best_k = 0
        # We'll check all k from 0 to n
        for k in range(n + 1):
            if k > 0:
                if s[k - 1] == '0':
                    pref0 += 1
            # now pref0 = number of '0' in s[0:k]
            pref1 = k - pref0
            if pref0 <= cnt1 and pref1 <= cnt0:
                best_k = k
        # minimal cost = n - best_k
        out_lines.append(str(n - best_k))

    sys.stdout.write("\n".join(out_lines))


solve()