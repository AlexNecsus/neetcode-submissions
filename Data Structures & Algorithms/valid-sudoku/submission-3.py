class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # first we check rows, than columns than 3x3 grids
        # if curr != "." we have temporary dictionary in which we have values through 1-9 
        # by using this temporary dict we check if after decrementing we look if any value became less than zero
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = cols = collections.defaultdict(set) # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True