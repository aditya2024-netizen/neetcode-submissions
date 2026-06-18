class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)) :
        #     for j in range(i+1,len(nums)):
        #         if (nums[i]+nums[j]) == target and i != j:
        #             return [i,j]
       
       seen = {}

       for index in range(len(nums)) :
        required = target - nums[index] 
        if required in seen:
            return [seen[required],index]
        else:
            seen[nums[index]] = index