class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            bit = n & 1     #used to extract last digit from a number 
            # if ans > 214748364:
            #     return 0;
            # if ans > 214748364 and bit > 7:
            #     return 0;
            ans = (ans << 1) | bit # used to append the extracted bit to answer after left shift of a bit in answer
            n >>= 1
        return ans
