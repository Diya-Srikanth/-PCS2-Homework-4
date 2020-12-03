import numpy as np


def counting(trans):
    a = []
    c = []
    for x in trans:
        x = list(x)
        n = len(x)
        A = x.count("A")
        C = x.count("C")
        G = x.count("G")
        T = x.count("T")

        a.append(A)
        a.append(C)
        a.append(G)
        a.append(T)
    final = [a[i * 4:(i + 1) * 4] for i in range((len(a) + 4 - 1) // 4)]
    data = np.array(final)
    pose = data.transpose()
    for x in pose:
        c.append(list(x))

    return c


def most_common(L):
    n = []
    most_common, num_most_common = Counter(L).most_common(1)[0]
    return most_common


with open("rosalind_cons.txt") as file:
    file = file.read()
    l = []
    n = []
    s = file.split()
    s = len(s[0]) - 1
    f = file.replace("\n", '')
    f = f.split(">")
    f.remove(f[0])
    for x in f:
        x = x[s:]
        x = [str(i) for i in x]
        l.append(x)
    data = np.array(l)
    trans = data.transpose()
    for x in trans:
        L = list(x)
        print(most_common(L))

    v = list(counting(trans))
    print("A: " + " ".join(str(x) for x in v[0]))
    print("C: " + " ".join(str(x) for x in v[1]))
    print("G: " + " ".join(str(x) for x in v[2]))
    print("T: " + " ".join(str(x) for x in v[3]))

