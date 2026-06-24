class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = set()
        for num in nums:
            if num not in arr:
                arr.add(num)
            
            else:
                arr.remove(num)
        
        ans = list(arr)[0]
       
                   

        return ans