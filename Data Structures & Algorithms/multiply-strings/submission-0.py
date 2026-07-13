class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        answer = [0] * (len(num1) + len(num2))
        index = 0
        final_ans = ""
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                p2 = i + j + 1
                p1 = i + j
                total = mul + answer[p2]
                answer[p1] += total // 10
                answer[p2] = total % 10

        
        while index < len(answer) - 1 and answer[index] == 0:
            index += 1

        for i in range(index,len(answer)):
            final_ans += str(answer[i])
        return final_ans