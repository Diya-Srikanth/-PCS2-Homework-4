from collections import Counter
a = sorted(input())
b = Counter(a).values()
print(*b)
