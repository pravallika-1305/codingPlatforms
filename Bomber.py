rows,columns,time = map(int,input().split())
def setup():
    input_grid = []
    grid_file = open("bomberman.txt","r")
    input_grid.append( list("*"*(columns + 2)))
    for _ in range(rows):
        input_grid.append(list("*" + grid_file.readline().strip() + "*"))
    input_grid.append(list("*"*(columns + 2)))
    return input_grid

def identify_bomblocations(input_grid):
    indices = []
    for i in range(1,rows + 1):
     for j in range(1,columns + 1):
       if input_grid[i][j] == "O":
             indices.append((i,j))
    return indices

def replace_with_bombs():
    second_grid = []
    for i in range(rows + 2):
        second_grid.append(list("O" * (columns + 2)))
    return second_grid

def generate_third_grid(indices_list,second_grid):
    for i in range(rows +  2):
        for j in range(columns + 2):
            for r,c in indices_list:
                if (i,j) == (r,c) :
                    second_grid[i][j] = second_grid[i][j].replace(second_grid[i][j],".")
                    second_grid[i - 1][j] =  second_grid[i - 1][j].replace(second_grid[i - 1][j],".")
                    second_grid[i + 1][j] =  second_grid[i + 1][j].replace(second_grid[i + 1][j],".")
                    second_grid[i][j - 1] =  second_grid[i][j - 1].replace(second_grid[i][j - 1],".")
                    second_grid[i][j + 1] = second_grid[i][j + 1].replace(second_grid[i][j + 1],".")
    return second_grid

def display(final_grid):
    for i in range(1,rows + 1):
        for j in range(1,columns + 1):
            print(final_grid[i][j],end = "")
        print()

count = 0
test_grid = setup()
while(count < time):
    indices_list = identify_bomblocations(test_grid)
    count = count + 1
    if count == time:
        display(test_grid)
        break
    second_grid = replace_with_bombs()
    count = count + 1
    if count == time:
        display(second_grid)
        break
    test_grid = generate_third_grid(indices_list,second_grid)
    count = count + 1
    if count == time:
        display(test_grid)
        break

