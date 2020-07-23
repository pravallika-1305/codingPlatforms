def remove_char(puzzle,ch,row,column):
    for j in range(1,len(puzzle)):
       puzzle[row][j] = puzzle[row][j].replace(ch,'_')
    for i in range(1,len(puzzle)):
        puzzle[i][column] = puzzle[i][column].replace(ch,'_')
    print(puzzle)

def inequality_constraint_propagator(puzzle, row, column, maximum, minimum):
    if(puzzle[row][column] == '>'):
       puzzle[row][column - 1] = puzzle[row][column - 1].replace(minimum,'_')
       puzzle[row][column + 1] = puzzle[row][column + 1].replace(maximum,'_')
    if(puzzle[row][column] == '<'):
       puzzle[row][column - 1] = puzzle[row][column - 1].replace(maximum,'_')
       puzzle[row][column + 1] = puzzle[row][column + 1].replace(minimum,'_')
    if(puzzle[row][column] == '^'):
       puzzle[row - 1][column] = puzzle[row - 1][column].replace(maximum,'_')
       puzzle[row + 1][column] = puzzle[row + 1][column].replace(minimum,'_')
    if(puzzle[row][column] == 'v'):
       puzzle[row - 1][column] = puzzle[row - 1][column].replace(minimum,'_')
       puzzle[row + 1][column] = puzzle[row + 1][column].replace(maximum,'_')
    print(puzzle)
#def update_puzzle(puzzle,row,column):

    #if(puzzle[row][column])
    
def max_in_string(strr):
    maximum_value = max([int(char) for char in strr])
    return maximum_value
def min_in_string(strr):
    minimum_value = min([int(char) for char in strr])
    return minimum_value
#string = "1234"
#print(max_in_string(string))
def generate_string(size): 
    num_list = [str(item) for item in range(1, size + 1)]
    strr = '' 
    for word in num_list:
        strr = strr + word
    return strr
print(generate_string(4))
#def swap_with_int()
puzzle = [['123','>','123'],
['123','123','123'],
['123','123','123']]

#remove_char(puzzle,'2',0,0)
inequality_constraint_propagator(puzzle,0,1,'3','1')
numbers = []
 

