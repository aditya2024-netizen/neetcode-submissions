class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}
        if len(s) == len(t):
            for ch in s:
                if ch in freq_s:
                    freq_s[ch] += 1
                else:
                    freq_s[ch] = 1
            for ch in t:
                if ch in freq_t:
                    freq_t[ch] += 1
                else:
                    freq_t[ch] = 1
            if freq_s == freq_t :
                return True
            else:
                return False
        else:
            return False

        
        