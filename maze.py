import helpers

# Your job is to develop this function
def find_path(board, row, col):
    # base step
    if not helpers.inbounds(board,row,col):
        return False
    if board[row][col] == helpers.markers.boundary:
        return False
    if board[row][col] == '*':
        return False
    if board[row][col] == helpers.markers.goal:
        return True    

    previous = board[row][col]
    board[row][col]= '*'
    if find_path(board,row,col+1):
        return True
    if find_path(board,row+1,col):
        return True
    if find_path(board,row,col-1):
        return True
    if find_path(board,row-1,col):
        return True    
    board[row][col] = previous
    return False

'''    
    a = find_path(board,row,col+1)
    b = find_path(board,row+1,col)
    c = find_path(board,row,col-1)
    d = find_path(board,row-1,col)
    if not (a or b or c or d):
        board[row][col]=previous
        return False
'''

board = helpers.get_board('board.txt')
helpers.print_board(board)
print('-' * 50)

find_path(board, 0, 0)

print('-' * 50)
helpers.print_board(board)
