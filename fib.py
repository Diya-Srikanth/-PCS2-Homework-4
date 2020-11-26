if __name__ == '__main__':
    a = list(map(int, input().split()))
    l = [1, 1]
    for i in range(a[0] - 2):
        x = l[-1] + l[-2] * a[1]
        l.append(x)
    print(l[-1])
