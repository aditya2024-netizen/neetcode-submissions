class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute-force
        # result = True
        # for num in nums:
        #     if nums.count(num) > 1 :
        #         result = True
        #     else:
        #         result = False
        # return result
        #optimal using set to store the number already seen
        seen_numbers = set()
        numbers = nums 
        flag = False
        for num in numbers:
            if num in seen_numbers:
                flag = True
            else:
                seen_numbers.add(num)

        return flag