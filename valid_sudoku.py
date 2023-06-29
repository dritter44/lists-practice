import collections

# for a given sudoku board, determine if it is valid (no repeating numbers in rows, 3x3 boxes, or columns)
def valid_sudoku(board):
    #initiate hashmap of hashes
    hash_map = {1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{}}

    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set) #key = (r/3, c/3)

    for r in range(9):

        for c in range(9):

            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r//3,c//3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])
    return True
