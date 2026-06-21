class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            if num in result :
                result[num]+=1
            else:
                result[num]=1
        
        freq_list= []
        for key,value in result.items() :
            freq_list.append((key,value))
        freq_list.sort(key=lambda x: x[1],reverse = True)
        ans = []
        for i in range(k):
            ans.append(freq_list[i][0])
        return ans


