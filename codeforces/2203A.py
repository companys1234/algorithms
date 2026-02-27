t = int(input())
import math
for _ in range(t):
    n,m,d = map(int,input().split())
    colv = int(1+(d/m))
    print(math.ceil(n/colv))