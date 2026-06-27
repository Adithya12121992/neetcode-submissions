class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Adithya Solution
        # sort and check , O(n log n ), O(1)
        '''nums = sorted(nums)
        prev = None
        for elem in nums:
            if prev != None:
                if prev == elem:
                    return True
            prev = elem
        return False'''
        # using set 
        # O(n), O(n)
        '''set1 = set()
        for elem in nums:
            if elem in set1:
                return True
            set1.add(elem)
        return False'''
        # easy solution 
        # O(n), O(n)
        return len(set(nums)) != len(nums)