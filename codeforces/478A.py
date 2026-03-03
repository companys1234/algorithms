c = list(map(int,input().split()))
b = 1
z = b*5
while z < sum(c):
    b += 1
    z = b*5
if z == sum(c):
    print(b)
else:
    print(-1)