class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for ans in matrix:
            for val in ans:
                if val == target:
                    return True
        return False