class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # straightforward solution -- Easy , but space is O(n)
        '''seen = set()
        for elem in nums:
            if elem not in seen:
                seen.add(elem)
            else:
                return elem'''
        # but we need O(1) solution w.r.t space
        nums = sorted(nums)
        prev = None
        for elem in nums:
            if prev is not None:
                if prev >= elem:
                    return elem
            prev = elem