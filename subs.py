with open('rosalind_subs.txt','r') as file:
    file = file.read()
    f = file.split()
    l=[]
    a = list(f[0])
    b = list(f[1])
    for i in range(len(a)):
        for j in range(i):
            if b == a[j:i]:
                l.append(j+1)
    print(*l)