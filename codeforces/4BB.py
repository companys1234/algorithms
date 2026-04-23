d, sumt = map(int, input().split())
mins = []
maxs = []
for _ in range(d):
    mint, maxt = map(int, input().split())
    mins.append(mint)
    maxs.append(maxt)

min_sum = sum(mins)
max_sum = sum(maxs)

if not (min_sum <= sumt <= max_sum):
    print('NO')
    exit()

# начинаем с минимальных значений
result = mins[:]
remain = sumt - min_sum

# распределяем остаток
for i in range(d):
    can_add = maxs[i] - result[i]
    add = min(remain, can_add)
    result[i] += add
    remain -= add

print('YES')
print(*result)