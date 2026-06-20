class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char for char in s if char.isalnum())
        reversed = ""
        for char in range(len(string) - 1 ,-1,-1):
            reversed+=string[char]
        
        if string.lower() == reversed.lower():
            return True
        return False
