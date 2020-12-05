def inc(A):
    LIS = [[] for _ in range(len(A))]
    LIS[0].append(A[0])
    for i in range(1, len(A)):
        for j in range(i):
            if A[j] < A[i] and len(LIS[j]) > len(LIS[i]):
                LIS[i] = LIS[j].copy()

        LIS[i].append(A[i])

    j = 0
    for i in range(len(A)):
        if len(LIS[j]) < len(LIS[i]):
            j = i

    print(*LIS[j])
    return ''


def dec(A):
    LIS = [[] for _ in range(len(A))]
    LIS[0].append(A[0])
    for i in range(1, len(A)):
        for j in range(i):
            if A[j] > A[i] and len(LIS[j]) > len(LIS[i]):
                LIS[i] = LIS[j].copy()

        LIS[i].append(A[i])

    j = 0
    for i in range(len(A)):
        if len(LIS[j]) < len(LIS[i]):
            j = i

    print(*LIS[j])
    return ''


if __name__ == '__main__':
    a = int(input())
    l = []
    c = []
    n = []
    final = []
    b = list(map(int, input().split()))
    print(inc(b))
    print(dec(b))