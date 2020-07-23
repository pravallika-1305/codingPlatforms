def identifying_turnovers(matrix,i,j):
    pos_list = []
    if matrix[i][j] == 1:
        pos_list.append(i)
    elif matrix[i][j] == 3:
        pos_list.append(i)
        pos_list.append(j)
    return pos_list

def turnover_indices(order,matrix):
    pos_list = []
    for i in range(1,order + 1):
        for j in range(1,order + 1):
            pos_list = pos_list + identifying_turnovers(matrix,i,j)
    return list(set(pos_list))

def final_operation(order,matrix):
    my_list = [i + 1 for i in range(order)]
    turnover_list =  turnover_indices(order,matrix)
    final_list = [x for x in my_list if x not in turnover_list]
    return(final_list)


order = int(input())
matrix = [[int(input()) for _ in range (order)] for _ in range(order)]
print(matrix)
print(final_operation(order,matrix))
