class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3,c//3]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[r//3,c//3].add(board[r][c])
        return True

#We iterate over all 81 cells, and each operation is O(1), so time is O(1).
#We use sets for rows, columns, and boxes, each storing at 
#most 9 elements, so space is also O(1).
# But if grid was N*N then time and space will be O(n^2)