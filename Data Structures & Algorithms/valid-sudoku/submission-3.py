from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_row = defaultdict(set)
        hash_col = defaultdict(set)
        hash_grid = defaultdict(set)

        for i in range(len(board)) :
            for j in range(len(board[i])) :
                if board[i][j] == "." :
                    continue
                if (board[i][j] in hash_row[i]) or (board[i][j] in hash_col[j]) or (board[i][j] in hash_grid[(i // 3 , j // 3)]) : 
                    return False
                else : 
                    hash_row[i].add(board[i][j])
                    hash_col[j].add(board[i][j])
                    hash_grid[(i // 3 , j // 3)].add(board[i][j])
        return True