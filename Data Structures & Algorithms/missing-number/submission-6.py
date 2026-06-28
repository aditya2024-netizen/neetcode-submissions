class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        upper_limit = len(nums)
        for i in range(upper_limit + 1):
            if i not in nums:
                return i
        return 0
    