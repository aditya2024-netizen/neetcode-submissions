class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # brute force
        # number =0
        # ans = []
        # for num in digits:
        #     print(number)
        #     number = number * 10 + num
        # number = number + 1
        # # print(number)
        # ans = [ int(d) for d in str(number)]

        # Optimal solution
        for i in range(len(digits) - 1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits

        