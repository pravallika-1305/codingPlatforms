def decrement(n):
    return n - 1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    a = list(filter(lambda x: x != 0, a))
    profit = 0
    while(len(a) != 0):
        profit = profit + a[0]
        a = list(map(decrement, a[1:]))
    print(profit)

