class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 0
        while(left <= right):
            # Mid speed 
            mid = left + (right - left) // 2

            #Total hours using the speed mid
            total_hrs = sum((pile + mid - 1)//mid for pile in piles)

            # if total_hrs is less than the limit move right to mid speed - 1
            # so that we could find even more smaller speed
            if total_hrs <= h:
                ans = mid
                right = mid - 1
            
            # if total_hrs is greater than the limit move the left to mid + 1 
            # so that we could find a valid speed
            elif total_hrs > h:
                left = mid + 1
        
        return ans
