n,a,b = map(int,input().split())
c = 0
for i in range(0,n-a):
    if i <= b:
        c += 1
print(c)