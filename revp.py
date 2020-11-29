def rev(a):
    l = []
    for x in a:
        if x == 'A':
            l.append("T")
        elif x == 'T':
            l.append("A")
        elif x == 'G':
            l.append('C')
        elif x == 'C':
            l.append('G')
    return l[::-1]


def ret(y):
    l = []
    for k in range(len(y) + 1):
        for z in range(k):
            if 4 <= len(y[z:k]) <= 12:
                l.append(y[z:k])
    return l


def ind(x, l):
    n = []
    m = []
    for i in range(len(x) + 1):
        for j in range(i):
            if 4 <= len(x[j:i]) <= 12:
                c = x[j:i]
                if c in l and c == rev(c):
                    print(j + 1, len(c))

    return ""


with open("rosalind_revp2.txt", 'r') as file:
    file = file.read()
    f = file.split()
    f.remove(f[0])
    f = " ".join(x for x in f)
    f = f.replace(" ", "")
    x = [str(i) for i in f]
    y = rev(x)
    l = ret(y)
    print(ind(x, l))
