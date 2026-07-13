class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 0
        while(left <= right):
            mid = left + (right - left) // 2
            total_hrs = sum((pile + mid - 1)//mid for pile in piles)
            if total_hrs <= h:
                ans = mid
                right = mid - 1
            
            elif total_hrs > h:
                left = mid + 1
        
        return ans
