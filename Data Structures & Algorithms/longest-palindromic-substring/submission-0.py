class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max_len = 0
        self.ret = ""
        for i in range(len(s)):
            self.expand(s, i, i)
            self.expand(s, i, i+1)
        return self.ret
    def expand(self, s, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        if self.max_len < (r-l-1):
            self.max_len = r-l-1
            self.ret = s[l+1:r]