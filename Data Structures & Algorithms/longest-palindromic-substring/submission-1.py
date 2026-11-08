class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max_len = 0
        self.string1 = ""
        for idx, char in enumerate(s):
            self.expand(idx, idx, s)
            self.expand(idx, idx+1, s)
        return self.string1
        
    def expand(self, l, r, word):
        while l>=0 and r<len(word) and word[l]==word[r]:
            l-=1
            r+=1
        if self.max_len<(r-l-1):
            self.max_len = r-l-1
            self.string1 = word[l+1:r]
        
