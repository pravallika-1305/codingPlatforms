mat,Y = [],[]
m,n = list(map(int,input().strip().split()))[:2]

for _ in range(m):
    mat.append(list(map(int,input().strip().split()))[:n])
for _ in range(m):
    Y.append(list(map(int,input().strip().split()))[:n])
res_list = [list(map(sum, zip(*t))) for t in zip(mat, Y)]

for i in res_list:
    print(*i)
