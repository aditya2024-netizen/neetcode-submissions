class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0
        while( left < right):
            curr_result = numbers[left] + numbers[right]
            if curr_result < target:
                left += 1
            
            elif curr_result > target:
                right -= 1
            
            elif curr_result == target:
                return [left + 1,right + 1]
