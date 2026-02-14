def min_ops_to_even(x):
    # минимальное кол-во операций, чтобы x стал чётным
    if x % 2 == 0:
        return 0
    else:
        return 1
def min_ops_to_div4(x):
    # минимальное кол-во операций, чтобы x стал делиться на 4
    r = x % 4
    if r == 0:
        return 0
    else:
        return 4 - r

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    z = []
    if k == 5:
        ops = min((5 - (x % 5)) % 5 for x in a)
        z.append(ops)
    elif k == 3:
        ops = min((3 - (x % 3)) % 3 for x in a)
        z.append(ops)
    elif k == 2:
        ops = min((2 - (x % 2)) % 2 for x in a)
        z.append(ops)
    elif k == 4:
        opt1 = min(min_ops_to_div4(x) for x in a)
        opt2 = [min_ops_to_even(x) for x in a]
        opt2 = sorted(opt2)
        z.append(min(opt1,(opt2[0]+opt2[1])))
    print(*z)

