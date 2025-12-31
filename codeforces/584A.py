n,t = map(int,input().split())
s = '9'
s2 = '1'
a = (int(int(n)*s))
b = int(s2+('1'*(int(n)-1)))
d = True
for i in range(b+1,a+1):
    if i % t == 0:
        print(i)
        d = False
        break
if d:
    print(-1)