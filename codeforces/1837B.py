t = int(input())
for _ in range(t):
    k = 1
    n = int(input())
    s = str(input())
    z = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            z += 1
            if z > k:
                k = z
        else:
            z = 1
    print(k+1)