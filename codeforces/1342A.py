t = int(input())
for _ in range(t):
    c = 0
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    b2 = (min(x,y))

    b3 = (max(x,y) - b2)
    b4 = (x+y) * a
    print(min(abs((b3*a)+(b2*b)),b4))