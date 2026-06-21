class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force
        # result = {}
        # for num in nums:
        #     if num in result :
        #         result[num]+=1
        #     else:
        #         result[num]=1
        
        # freq_list= list(result.items())
        # freq_list.sort(key=lambda x: x[1],reverse = True)
        # ans = []
        # for i in range(k):
        #     ans.append(freq_list[i][0])
        # return ans
        # Optimal Soln 
        frequency = {}
        bucket = [[] for _ in range(len(nums)+1)]
        result = []
        for num in nums :
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        for key,value in frequency.items():
            bucket[value].append(key)
        
        for i in range(len(bucket) - 1 , -1 , -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

            
    



