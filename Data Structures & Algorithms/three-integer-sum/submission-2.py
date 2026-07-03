class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_array = sorted(nums)
        ans = []

        for index in range(len(sorted_array) - 2):
            # num = sorted_array[index]
            # comparing with the previous element 
            # if both previous and current element are same then don't exectue that part 
        
            if (index > 0  and sorted_array[index] == sorted_array[index - 1]):
                continue

            left = index + 1
            right = len(sorted_array) - 1
            while (left < right):
                total = sorted_array[left] + sorted_array[right] + sorted_array[index]

                if total < 0 :
                    left += 1
                
                elif total > 0 :
                    right -= 1
                
                else : 
                    ans.append([sorted_array[index],sorted_array[left],sorted_array[right]])
                    left += 1
                    right -= 1
                    while(left < right and sorted_array[left - 1] == sorted_array[left]):
                        left += 1
                
                    while(left < right and sorted_array[right + 1] == sorted_array[right]):
                        right -= 1

        return ans