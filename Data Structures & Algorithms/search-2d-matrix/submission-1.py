class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute Force
        # for ans in matrix:
        #     for val in ans:
        #         if val == target:
        #             return True
        # return False
        # Optimal 
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        left = 0
        right = total - 1

        while(left <= right):
            mid = (left + right)/ 2
            row = int(mid // cols)
            col = int(mid % cols)
            val = matrix[row][col]
            if( val == target):
                return True
            
            elif(val < target):
                left += 1
            
            else:
                right -= 1
            
        
        return False