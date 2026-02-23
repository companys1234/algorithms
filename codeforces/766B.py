n = int(input())
a = list(map(int,input().split()))
z = sorted(a,reverse=True)
an = sorted(a)
d = True
for i in z:
    an.remove(i)
    if d == False:
        break
    for j in range(len(an)-1):
        if an[j] + an[j+1] > i:
            print('YES')
            d = False
            break
if d:
    print('NO')