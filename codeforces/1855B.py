import math
t  = int(input())
for _ in range(t):
    n = int(input())
    d = math.ceil(math.sqrt(n))
    max_i = 0
    i =0
    for y in range(1,d+1):
        if n%y == 0:
            i += 1
            if i > max_i:
                max_i = i
        else:
            i = 0
            break
        if i > max_i:
            max_i = i
    print(max_i)