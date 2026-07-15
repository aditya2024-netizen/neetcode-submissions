class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1 
        left = 0 
        right = len(matrix[0]) - 1
        lst = []
        while top <= bottom and left <= right:
            # top elements
            for index in range(left,right + 1):
                lst.append(matrix[top][index])
            top += 1

            # right elements
            for index in range(top,bottom + 1):
                lst.append(matrix[index][right])
            right -= 1

            # bottom elements
            if top <= bottom:
                for index in range(right,left - 1,-1):
                    lst.append(matrix[bottom][index])
                bottom -= 1

            # left elements
            if left <= right:
                for index in range(bottom,top - 1,-1):
                    lst.append(matrix[index][left])
                left += 1
        
        return lst