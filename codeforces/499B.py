n,m = map(int,input().split())
dictx = {}
for _ in range(m):
    a, b = map(str, input().split())
    dictx[a] = b

c = list(str(input().split()))
for i in c:
    if len(i) < len(dictx[i]):
        print(i)
    if len(i) > len(dictx[i]):
        print(dictx[i])
    elif len(i) == len(dictx[i]):
        print(i)