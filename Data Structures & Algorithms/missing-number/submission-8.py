class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        upper_limit = len(nums)
        # for i in range(upper_limit + 1):
        #     if i not in nums:
        #         return i
        # return 0
        # real_sum = (upper_limit * (upper_limit + 1 ) // 2 )
        # actual_sum = sum(nums)
        # return real_sum - actual_sum
        ans = 0
        for i in range(upper_limit):
            ans^=i
            ans^=nums[i]
        ans^=upper_limit
        return ans
    