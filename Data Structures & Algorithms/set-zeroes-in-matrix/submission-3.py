class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # optimal
        first_row_is_zero = False
        first_col_is_zero = False

        # check for 1st row contains zero or not 
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                first_row_is_zero = True
        
         # check for 1st column contains zero or not 
        for j in range(len(matrix)):
            if matrix[j][0] == 0:
                first_col_is_zero = True
        
        # marking of 1st  row and column to zero if other rows or colms contains zero
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_is_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if first_col_is_zero:
            for j in range(len(matrix)):
                matrix[j][0] = 0
              
        
