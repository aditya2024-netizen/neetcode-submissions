class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        right = 0
        longest = 0

        for i in range(len(s)):
            while s[right] in seen:
                left = max( left,seen[s[right]] + 1)
                break
            seen[s[right]] = right
            longest = max(longest,right - left + 1)
            right += 1
        
        return longest

            
