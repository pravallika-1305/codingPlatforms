def isEven(n):
    return n % 2 == 0

def check(n):
    exists = False
    while(n > 1):
        n //= 2
        if not(isEven(n)):
            exists = True
            break
        else:
            continue
    return (exists, n)

for _ in range(int(input())):
    TS = int(input())
    if TS == 1:
        print(0)
    elif not(isEven(TS)):
        print( TS // 2 )
    else:
        exists,n = check(TS)
        if exists:
            print(n // 2)
        else:
            print(0)

            