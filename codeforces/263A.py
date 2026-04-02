s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))
s3 = list(map(int,input().split()))
s4 = list(map(int,input().split()))
s5 = list(map(int,input().split()))
z = [s1,s2,s3,s4,s5]
i = 0
l = 0
for g in range(5):
    for r in range(5):
        if z[g][r] == 1:
            l = r+1
            i = g+1
            break


i2 = abs(3-i)
l2 = abs(3-l)
print(i2+l2)