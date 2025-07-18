# -*- coding: utf-8 -*-
"""433B

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J9W8aE_2E3PMqFVkoKAs_g8xTifQE6k1
"""

import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    n = int(data[idx])
    idx += 1
    v = list(map(int, data[idx:idx + n]))
    idx += n

    # Префиксные суммы для исходного массива
    prefix_v = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_v[i] = prefix_v[i - 1] + v[i - 1]

    # Отсортированный массив и его префиксные суммы
    u = sorted(v)
    prefix_u = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_u[i] = prefix_u[i - 1] + u[i - 1]

    m = int(data[idx])
    idx += 1
    output = []
    for _ in range(m):
        t = int(data[idx])
        l = int(data[idx + 1])
        r = int(data[idx + 2])
        idx += 3

        if t == 1:
            res = prefix_v[r] - prefix_v[l - 1]
        else:
            res = prefix_u[r] - prefix_u[l - 1]
        output.append(str(res))

    print('\n'.join(output))

if __name__ == "__main__":
    main()