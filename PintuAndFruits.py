for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    fruit_list = list(map(int,input().strip().split()))[:n] 
    price_list = list(map(int,input().strip().split()))[:n]
    total = 0
    pay_list = []
    for i in range(len(fruit_list) - 1):
        total = price_list[i]
        for j in range(i + 1,len(fruit_list)):
            if fruit_list[j] == fruit_list[i]:
                total += price_list[j]
        pay_list.append(total)
        if len(pay_list) == len(set(fruit_list)):
            break
    print(min(pay_list))

    