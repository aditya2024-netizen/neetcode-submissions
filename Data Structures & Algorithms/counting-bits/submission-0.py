class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n+1):
            count = 0
            while num != 0 :
                count += 1 
                num = num & (num - 1)
            result.append(count)
        return result