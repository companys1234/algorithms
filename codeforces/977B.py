t = int(input())
s = str(input())
k = {}
x = [s[a:a + 2] for a in range(0, len(s), 1)]
for i in x:
    if i not in k.keys():
        k[i] = 1
    else:
        k[i] += 1

m = max(k.values())
for k, v in k.items():
    if v == m:
        print(k)
        break
