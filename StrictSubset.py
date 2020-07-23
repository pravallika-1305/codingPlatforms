set_A, n = set(input().split()), int(input())
cnt = 0
check = True
for _ in range(n):
    if not set_A.issuperset(set(input().split())):
        check = False
        break
print(check)