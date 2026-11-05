class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.expand(s, i, i)
            result += self.expand(s, i, i+1)
        return result
    def expand(self, s, l, r):
        count = 0
        while l>=0 and r<len(s) and s[l]==s[r]:
            count+=1
            l-=1
            r+=1
        return count 