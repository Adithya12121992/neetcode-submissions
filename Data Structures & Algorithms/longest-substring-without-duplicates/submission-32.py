class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        unique_chars = set()
        for r in range(len(s)):
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l+=1
            unique_chars.add(s[r])
            result = max(result, (r-l)+1)
            '''if s[r] not in unique_chars:
                unique_chars.add(s[r])
            else:
                while s[l]!=s[r]:
                    unique_chars.remove(s[l])
                    l+=1
                l+=1
            result = max(result, (r-l)+1)'''
        return result