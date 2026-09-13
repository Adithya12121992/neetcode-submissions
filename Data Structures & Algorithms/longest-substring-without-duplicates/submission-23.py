class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dict1 = set()
        res = 0
        for r in range(len(s)):
            while s[r] in dict1:
                dict1.remove(s[l])
                l+=1
            dict1.add(s[r])
            res = max(res, r-l+1)
        return res
