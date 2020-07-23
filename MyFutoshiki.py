space = '_'
DIGITS = '123456789'
def setup(filename):
    lines = [line.strip() for line in open(filename)]
    size = 1 + len(lines[0]) // 2
    digits = DIGITS[:size]
    my_square = [[digits] * size for i in range(size)]
    unedited_constraints = []
    for line_num, line in enumerate(lines):
        unedited_constraints.append(line)
        if line_num % 2 == 0:
            filled = line[::2]
            for j, occupied in enumerate(filled):
                if occupied != space:
                    #print(line_num // 2)
                    my_square[line_num // 2][j] = occupied
    return my_square, unedited_constraints

def transform_constraints(constraints):
    constraint_tuples = []
    for i,constraint in enumerate(constraints):
        r = i // 2
        for j,ch in enumerate(constraint):
            c = j // 2
            if ch in "<>":
                constraint_tuples.append(((r,c),ch,(r,c + 1)))
                print(r,c,c + 1,ch)
            elif ch in "^v":
                ch = "<" if ch == "^" else ">"
                constraint_tuples.append(((r,c),ch,(r + 1,c)))
    return constraint_tuples


def update_grid(grid):
    size = len(grid[0])
    print(len(grid) * len(grid[0]))
    print(len(''.join([''.join(i) for i in grid])))
    for i in range(size):
        for j in range(size):
            row,col = (i,j)
            if len(grid[row][col]) ==  1:
                size = len(grid[row])
                ch = grid[row][col]
                for r in range(size):
                    if r != row and len(grid[r][col]) > 1:
                        grid[r][col] = grid[r][col].replace(ch,"")
                for c in range(size):
                    if c != col and len(grid[row][c]) > 1:
                        grid[row][c] = grid[row][c].replace(ch,"")
    return grid

"""def update_cell_in_grid(grid):
    size = len(grid[0])
    for i in range(size):
        line = ''.join(grid[i])
        print(line, '^^^^')
        for num in set(line):
            print(line.count(num),'____')
            if line.count(num) == 1:
                for j in range(size):
                    print(num, grid[i][j], '+++++')
                    if num in grid[i][j]:
                        grid[i][j] = num
                        print(num, grid[i][j], '+++++')
    return grid"""
def deterministic_cell(grid):
    size = grid[0]
    least_length= min([len(grid[i][j]) for i,j in range(size)])
    for i in range(size):
        for j in range(size):
            if len(grid[i][j]) == least_length:
                return i,j 
#print(less_than_zero)
def update_constraints(grid,constraints):
    #cell_tuple = deterministic_cell(grid)
    # size = len(grid[0])
    for constraint in constraints:
        lhs,rel,rhs = constraint
        r1,c1 = lhs
        r2,c2 = rhs
        """if len(set(lhs) & set(rhs)) == 0:
            continue"""
        if rel == '<':
            if max(grid[r1][c1]) == max(grid[r2][c2]):
               grid[r1][c1] = grid[r1][c1].replace(max(grid[r1][c1]),"")
               grid[r2][c2] = grid[r2][c2].replace(min(grid[r2][c2]),"")
            if min(grid[r1][c1]) == min(grid[r2][c2]):
                grid[r2][c2] == grid[r2][c2].replace(min(grid[r2][c2]),"")
        if rel == '>':
            if min(grid[r1][c1]) == min(grid[r2][c2]) :
                grid[r2][c2] = grid[r2][c2].replace(max(grid[r2][c2]),"")
                grid[r1][c1] = grid[r1][c1].replace(min(grid[r1][c1]),"")
            if max(grid[r1][c1]) == max(grid[r2][c2]):
                grid[r2][c2] == grid[r2][c2].replace(max(grid[r2][c2]),"")
    return grid

grid,constraints = setup("grid.txt")
print(grid)
print(constraints)
constraints = transform_constraints(constraints)
print(constraints)

"""
grid = update_cell_in_grid(grid)
print(grid)
"""

while len(grid) * len(grid[0]) < len(''.join([''.join(i) for i in grid])):
    grid = update_grid(grid)
    grid = update_constraints(grid,constraints)
print(grid)

