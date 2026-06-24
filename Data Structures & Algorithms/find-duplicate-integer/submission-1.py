class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # straightforward solution -- Easy , but space is O(n)
        seen = set()
        for elem in nums:
            if elem not in seen:
                seen.add(elem)
            else:
                return elem