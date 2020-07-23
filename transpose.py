def transpose(m):
    t_matrix = [*zip(*m)]
    return t_matrix

m,n = list(map(int,input().strip().split()))[:2] 
mat = []
for _ in range(m):
    mat.append(list(map(int,input().strip().split()))[:n])
result = transpose(mat)
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j],end = " ")
    print()