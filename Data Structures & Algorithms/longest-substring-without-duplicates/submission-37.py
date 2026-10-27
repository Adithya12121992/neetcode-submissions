class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2 pointer solution , sliding window 
        if len(s) ==0:
            return 0
        elif len(s) == 1:
            return 1
        l = 0
        max_val = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            max_val = max(max_val, (r-l)+1)
        return max_val
                
