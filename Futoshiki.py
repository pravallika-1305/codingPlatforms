def get_neighbours(puzzle,i,j):
    neighbours = [None]*4
    try:
        neighbours[0] = puzzle[j][i+1]
    except IndexError:
        pass
    try:
        neighbours[1] = puzzle[j+1][i]
    except IndexError:
        pass
    try:
        neighbours[2] = puzzle[j][i-1]
    except IndexError:
        pass
    try:
        neighbours[3] = puzzle[j-1][i]
    except IndexError:
        pass

    return neighbours
