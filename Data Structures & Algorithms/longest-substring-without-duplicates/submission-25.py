class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        dict1 = {}
        l = 0
        for r in range(len(s)):
            if s[r] not in dict1:
                dict1[s[r]] = r
            else:
                while s[l]!=s[r]:
                    del dict1[s[l]]
                    l+=1
                del dict1[s[l]]
                dict1[s[r]] = r
                l+=1
            res = max(res, r-l+1)
        return res
