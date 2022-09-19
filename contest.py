import math
d = input().split()
s = len(d[0])
n = int(d[0])
x = 0
a = int(d[1])
b = int(d[2])
k = []
for i in range(10):
    if i != a and i != b:
        k.append(str(i))
for i in range(n):
    r = str(i)
    j = 0
    for t in r:
        if t in k:
            j = 1
    if not j:
        x += 1
print(x)