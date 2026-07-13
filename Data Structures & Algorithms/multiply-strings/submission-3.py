class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        m = len(num1)
        n = len(num2)
        answer = [0] * (m + n)
        index = 0
        
        # multiplying each element
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                p2 = i + j + 1
                p1 = i + j
                total = mul + answer[p2]
                answer[p1] += total // 10
                answer[p2] = total % 10

        # finding the first non zero element
        while index < len(answer) - 1 and answer[index] == 0:
            index += 1

        # converting the answer array to string form 
        final_answer = "".join([str(d) for d in answer[index:]])

        return final_answer
