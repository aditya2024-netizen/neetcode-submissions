class Solution:
    def trap(self, height: List[int]) -> int:
        # brute-force
        # leftMax = [0]*(len(height))
        # rightMax = [0] * (len(height))
        # water = 0
        # leftMax[0] = height[0]
        # rightMax[-1] = height[-1]

        # for index in range(1,len(height)):
        #     leftMax[index] = max(height[index],leftMax[index - 1])
        
        # for index in range(len(height) - 2,-1,-1):
        #     rightMax[index] = max(height[index],rightMax[index + 1])
 
        # for index in range(len(height)):
        #     water += max(0,min(leftMax[index],rightMax[index]) - height[index])
        # return water

        # optimal
        left = 0
        right = len(height) - 1
        water = 0
        leftMax = 0
        rightMax = 0

        while(left < right):
            if height[left] < height[right]:
                leftMax = max(leftMax,height[left])
                water += leftMax - height[left]
                left += 1
            
            else:
                rightMax = max(rightMax,height[right])
                water += rightMax  - height[right]
                right -= 1
            
        return water
