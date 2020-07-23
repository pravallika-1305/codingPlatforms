for _ in range(int(input())):
    n, k = map(int, (input().split()))
    prices = list(map(int,input().strip().split()))[:n]
    revenue_lost = 0
    for i in prices:
        if i > k:
            revenue_lost += (i - k)
    print(revenue_lost)
            