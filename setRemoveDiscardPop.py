n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    x = input().split()
    if len(x) == 1:
        s.pop()
    elif x[0] == 'remove':
        try:
            s.remove(int(x[1]))
        except:
            next
    elif x[0] == 'discard':
        s.discard(int(x[1]))
print(sum(s))
