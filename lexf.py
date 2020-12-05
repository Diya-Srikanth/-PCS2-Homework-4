from itertools import permutations

if __name__ == '__main__':
    a = input()
    c = []
    n = []
    b = int(input())
    listed = a.split()
    f = list(permutations(listed, b))
    for x in f:
        string = list(x)
        c.append(string)

    for i in range(len(listed)):
        sim = [listed[i]] * b
        n.append(sim)
    data = n + c
    final = sorted(data)
    for x in final:
        print("".join(y for y in x))
