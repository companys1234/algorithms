n,m = map(int,input().split())
s = 0
s = n + n // (m - 1)
if n % (m - 1) == 0:
    s -= 1
print( s)
