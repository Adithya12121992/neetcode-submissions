class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        seen = set()
        max_cnt = 0
        for elem in set1:
            if elem in seen:
                continue
            interim_cnt = 0
            while elem in set1:
                elem+=1
                interim_cnt+=1
                seen.add(elem)
            max_cnt = max(max_cnt, interim_cnt)
        return max_cnt