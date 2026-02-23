pos = input(str())
inp = input(str())
vocab = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m',',','.','/']
z = []
if pos == 'R':
    for i in inp:
        u = vocab.index(i)
        if u-1 == -1:
            z.append(vocab[u])
        else:
            z.append(vocab[u-1])
else:
    for i in inp:
        u = vocab.index(i)
        if u+1 > len(vocab)-1:
            z.append(vocab[u])
        else:
            z.append(vocab[u+1])
print(''.join(z))