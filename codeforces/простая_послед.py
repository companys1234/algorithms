t = int(input())
print(3%4,4%2,2%1)
for _ in range(t):
    n = int(input())
    if n == 2:
        print(2,1)
    else:
        z = [i for i in range(n,0,-1)]
        z[0], z[1] = z[1], z[0]

        print(*z)