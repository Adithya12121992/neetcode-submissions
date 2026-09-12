class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set1 = set(nums)
        seen = set()
        max_val = 1
        for elem in set1:
            if elem in seen:
                continue
            interim_val = 0
            while elem in set1:
                interim_val +=1
                seen.add(elem)
                elem+=1
            max_val = max(max_val, interim_val)
        return max_val