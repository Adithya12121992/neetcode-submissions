class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        min_val = min(nums)
        max_val = max(nums)
        set1 = set(nums)
        res = 0
        for val in nums:
            if val-1 not in set1:
                cnt = 0
                while True:
                    if val in set1:
                        cnt+=1
                        val+=1
                    else:
                        break
                    res = max(res, cnt)
        return res

