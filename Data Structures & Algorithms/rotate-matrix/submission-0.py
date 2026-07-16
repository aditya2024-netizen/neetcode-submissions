class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # doing matrix transpose
        for  i in range(len(matrix[0])):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        # reverse each element in the rows 
        for row in matrix:
            row.reverse()
        
        
       
       
