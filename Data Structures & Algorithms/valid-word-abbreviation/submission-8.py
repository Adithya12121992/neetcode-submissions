class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i+=1
                j+=1
            elif abbr[j].isnumeric():
                num_val = ''
                while j < len(abbr) and abbr[j].isnumeric():
                    num_val+=abbr[j]
                    j+=1
                if num_val[0] == '0':
                    return False
                else:
                    num_val = int(num_val)
                i+=num_val
            else:
                return False
        return i==len(word) and j==len(abbr)
