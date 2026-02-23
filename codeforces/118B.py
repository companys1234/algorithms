
def fg(n,k,o):
    z = []
    mid = n-1
    #h = ' '
    sup = o+2
    #print(o-mid)
    for i in range(0,mid):
        z.append(str(i))
    for i in range(mid, -1, -1):
        z.append(str(i))
    lg = len(z)
    #print('g',lg)
    if o == mid:
        pass
    else:
        z.insert(0, ((abs(mid-o)*2)-1) * ' ')
    return print(*z)

n = int(input())
n += 1
for i in range(1, n):
    fg(i,n,n-1)
for i in range(n, 0, -1):
    fg(i,n,n-1)

