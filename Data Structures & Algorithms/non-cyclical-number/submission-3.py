class Solution:
    def isHappy(self, n: int) -> bool:
        # intermediate solution can be improved using floyd's cycle detection
        def add_digits(number):
            result = 0
            while (number != 0):
                digit = number % 10
                result += digit * digit
                number //= 10
            return result

        num = n
        seen = set()
        while num != 1:
            if num in seen:
                return False
            else:
                seen.add(num)
                num = add_digits(num)
        return True
