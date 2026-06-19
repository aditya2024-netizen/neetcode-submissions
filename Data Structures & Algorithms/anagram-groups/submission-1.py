class Solution:
    def frequency_count(self,word):
        freq_count = [0]*26
        for char in word:
            index = ord(char)-ord('a')
            freq_count[index] += 1
        return tuple(freq_count)
  
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute Force
        # result ={}

        # for word in strs:
        #     sorted_word = "".join(sorted(word))
        #     if sorted_word in result:
        #         result[sorted_word].append(word)
            
        #     else:
        #         result[sorted_word] = [word]
        # return list(result.values())

        # Optimal
        result = {}
        for word in strs:
            ans = self.frequency_count(word)
            if ans in result:
                result[ans].append(word)
            else:
                result[ans] = [word]

        return list(result.values())


           





        