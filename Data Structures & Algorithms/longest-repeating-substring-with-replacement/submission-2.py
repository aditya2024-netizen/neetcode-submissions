class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_freq = 0
        longest = 0
        for right in range(len(s)):

            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
            
            max_freq = max(max_freq,freq[s[right]])

            window = right - left + 1

            if ( window - max_freq ) > k:
                freq[s[left]] -= 1
                left += 1

            longest = max(longest,right - left + 1)
        return longest

            

            



            