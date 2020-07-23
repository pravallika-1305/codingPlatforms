def isPrime(n):
    if n == 1:
        return False
    if n in [2,3,5,7]:
        return True
    if n % 2 == 0:
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r = r + 2
    return True
		
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    final_list = list(filter(lambda x : isPrime(x),range(a,b)))
    for i in final_list:
        print(i)

	