import helpers

# Your job is to develop this function
def find_path(board, row, col, count):
    # base step
    count += 1
    if not helpers.inbounds(board,row,col):
        helpers.indent_print(count,'Out of Bounds')
        return False
    if board[row][col] == helpers.markers.boundary:
        helpers.indent_print(count,'Hit the wall')
        return False
    if board[row][col] == '*':
        helpers.indent_print(count,'Been There')
        return False
    if board[row][col] == helpers.markers.goal:
        helpers.indent_print(count,'Okay')
        return True    
    previous = board[row][col]
    board[row][col]= '*'
    helpers.indent_print(count,'Ok')
    if find_path(board,row,col+1,count):
        helpers.indent_print(count,'right')
        return True
    if find_path(board,row+1,col,count):
        helpers.indent_print(count,'down')
        return True
    if find_path(board,row,col-1,count):
        helpers.indent_print(count,'left')
        return True
    if find_path(board,row-1,col,count):
        helpers.indent_print(count,'up')
        return True    
    board[row][col] = previous
    helpers.indent_print(count,'dead end')
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

find_path(board, 0, 0, 0)

print('-' * 50)
helpers.print_board(board)
