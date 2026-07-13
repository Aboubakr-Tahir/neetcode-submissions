class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_set = collections.defaultdict(set)
        row_set = collections.defaultdict(set)
        carr_set = collections.defaultdict(set)
        for row in range(9) :
            for col in range(9) :
                if board[row][col] == "." :
                    continue
                if board[row][col] in row_set[row] or board[row][col] in col_set[col] :
                    return False
                if board[row][col] in carr_set[(row//3,col//3)] :
                    return False
                row_set[row].add(board[row][col])
                col_set[col].add(board[row][col])
                carr_set[(row//3,col//3)].add(board[row][col])
        return True