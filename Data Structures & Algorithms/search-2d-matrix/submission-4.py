class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bot = len(matrix) - 1
        top = 0
        while top <= bot :
            middle = (top+bot) // 2
            if target<matrix[middle][0]:
                bot = middle - 1
            elif target > matrix[middle][-1] :
                top = middle + 1
            else :
                break
        if top > bot :
            return False 
        row = middle
        start = 0
        end = len(matrix[middle]) - 1
        while start <= end :
            middle = (start + end) // 2
            if target < matrix[row][middle] :
                end = middle -1
            elif target > matrix[row][middle] :
                start = middle + 1
            elif matrix[row][middle] == target:
                return True 
        return False