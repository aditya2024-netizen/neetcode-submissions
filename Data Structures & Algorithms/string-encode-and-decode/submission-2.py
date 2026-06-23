class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string+=f"{len(word)}#{word}"
        
        return string

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            j = i
            while ( s[j] != "#"):
                j += 1
            length = int(s[i:j])
            start_index = j + 1
            end_index = j + 1 + length
            word = s[start_index:end_index]
            lst.append(word)
            i = end_index
        return lst

       