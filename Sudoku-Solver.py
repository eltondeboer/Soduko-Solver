import pprint


def solve(bo):
    find = findEmpty(bo)
    if find:
        row, col = find
    else:
        return True
    
    for i in range(1,10):
        if valid_num(bo, (row,col), i):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0

    return False

def valid_num (bo, pos, num):

    #Checks row
    for i in range(0,len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        
    #Checks column
    for i in range(0,len(bo)):
        if bo[i][pos[1]] == num and pos [0] != i:
            return False
    
    #Checks box

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

            

def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    
    return None


board = [
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 3],
    [0, 7, 4, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 2],
    [0, 8, 0, 0, 4, 0, 0, 1, 0],
    [6, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 7, 8, 0],
    [5, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0]
]

pp = pprint.PrettyPrinter(width=41, compact= True)
solve(board)
pp.pprint(board)