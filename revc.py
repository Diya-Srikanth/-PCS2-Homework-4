if __name__ == '__main__':
    a = input()
    l =[]
    for x in a:
        if x == 'A':
            l.append("T")
        elif x == 'T':
            l.append("A")
        elif x =='G':
            l.append('C')
        elif x == 'C':
            l.append('G')
    l.reverse()
    print("".join(y for y in l))