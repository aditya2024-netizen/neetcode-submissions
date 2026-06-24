class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # intermediate
        # left_product = list(1 for _ in range(len(nums)))
        # right_product = list(1 for _ in range(len(nums)))
        # result = list(1 for _ in range(len(nums)))
        # j = nums - 1 
        # for index in range(len(nums)):
        #     if ( index == 0): continue
        #     left_product[index] = left_product[index - 1] * nums[index - 1]

        # for index in range(len(nums) - 1,-1,-1):
        #     if ( index == len(nums) - 1): continue
        #     right_product[index] = right_product[index + 1] * nums[index + 1]
            
        
        # print(left_product)
        # print(right_product)
        # for index in range(len(left_product)):
        #     result[index] = left_product[index] * right_product[index]
        # print(result)
        result = list(1 for _ in range(len(nums)))
        right = 1 
        left = 1
        for index in range(len(nums)):
            result[index] *= left
            left *= nums[index] 

        for index in range(len(nums) - 1, -1, -1):
            result[index] *= right
            right *= nums[index]
           
        
    

        return result;
