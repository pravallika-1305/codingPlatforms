
my_list = list(map(int,input().strip().split()))[:2] 
n = my_list[0]
m = my_list[1]
happiness = 0

a = list(map(int,input().strip().split()))[:n] 
b = list(map(int,input().strip().split()))[:m]
c = list(map(int,input().strip().split()))[:m]
b = set(b)
c = set(c)
flag = 0
for i in a:
    if i in b:
        happiness = happiness + 1
    if i in c:
        happiness = happiness - 1
print(happiness)
