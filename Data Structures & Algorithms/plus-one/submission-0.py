class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number =0
        ans = []
        for num in digits:
            print(number)
            number = number * 10 + num
        number = number + 1
        # print(number)
        ans = [ int(d) for d in str(number)]
        
        return ans

        