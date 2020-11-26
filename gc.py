with open("rosalind_gc.txt", 'r') as file:
    l = []
    k = []
    file = file.read()
    f = file.replace("\n", '')
    f = f.split(">")
    f.remove(f[0])
    for i in range(len(f)):
        a = len(f[i]) - 13
        b = f[i].count('G')
        c = f[i].count('C')
        p = round((((b + c) / a) * 100), 6)
        l.append(p)
    for x in range(len(l)):
        if max(l) == l[x]:
            v = f[x]
    print(v[:13])
    print(max(l))



