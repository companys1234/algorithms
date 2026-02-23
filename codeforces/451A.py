n,m = map(int,input().split())
s = 'Akshat'
a = 0
while n >= 0 or m >= 0:
    a += 1
    if a % 2 != 0:
        s  = 'Akshat'
    else:
        s = 'Malvika'
    n -= 1
    m -= 1
    if n == 0 or m == 0:
        break

print(s)