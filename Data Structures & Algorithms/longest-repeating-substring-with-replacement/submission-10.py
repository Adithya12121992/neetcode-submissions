class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict1 = defaultdict(int)
        l = r = 0
        result = 0
        while r<len(s):
            dict1[s[r]]+=1
            if (r-l+1) > max(dict1.values())+k:
                dict1[s[l]]-=1
                l+=1
            result = max(result, r-l+1)
            r+=1
        return result