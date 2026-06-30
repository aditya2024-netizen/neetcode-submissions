class Solution:
    def reverse(self, x: int) -> int:
        # optimal
        absolute = abs(x)
        rev  = 0
        if x < 0 :
            sign = -1
        else:
            sign = 1
        while absolute!=0:
            digit = absolute%10
            if rev > 214748364:
                return 0

            if rev == 214748364 and digit > 7:
                return 0
            rev = rev*10 + digit
            absolute//=10
        rev *= sign
        return rev
