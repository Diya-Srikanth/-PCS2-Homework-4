import numpy as np


def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0]) - i + 1):
                if j > len(substr) and is_substr(data[0][i:i + j], data):
                    substr = data[0][i:i + j]
    return substr


def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


with open("rosalind_lcsm.txt") as file:
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
        l.append(x)
    data = np.array(l)
    print(long_substr(data))
