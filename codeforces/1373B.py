t = int(input())
for _ in range(t):
    s = str(input())
    e1 = s.count('1')
    e2 = s.count('0')
    pairs = min(e1,e2)
    if pairs % 2 == 0:
        print('NET')
    else:
        print('DA')