def increase(A):
    inc = [[] for _ in range(len(A))]
    inc[0].append(A[0])
    for i in range(1, len(A)):
        for j in range(i):
            if A[j] < A[i] and len(inc[j]) > len(inc[i]):
                inc[i] = inc[j].copy()

        inc[i].append(A[i])

    j = 0
    for i in range(len(A)):
        if len(inc[j]) < len(inc[i]):
            j = i

    print(*inc[j])
    return ''


def decrease(A):
    dec = [[] for _ in range(len(A))]
    dec[0].append(A[0])
    for i in range(1, len(A)):
        for j in range(i):
            if A[j] > A[i] and len(dec[j]) > len(dec[i]):
                dec[i] = dec[j].copy()

        dec[i].append(A[i])

    j = 0
    for i in range(len(A)):
        if len(dec[j]) < len(dec[i]):
            j = i

    print(*dec[j])
    return ''


if __name__ == '__main__':
    a = int(input())
    b = list(map(int, input().split()))
    print(increase(b))
    print(decrease(b))
