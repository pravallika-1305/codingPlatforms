import numpy as np
for _ in range(int(input())):
    n = int(input())
    a = np.array(input().split(),int)
    b = np.sort(a)
    diff = 1000000000
    for i in range(b.size - 1):
        if b[i + 1] - b[i] < diff:
            diff = b[i + 1] - b[i]
    print(diff)