class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # doing matrix transpose
        for i in range(len(matrix[0])):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # making each row reverse using  two pointer
        for row in matrix:
            left = 0
            right = len(row) - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
