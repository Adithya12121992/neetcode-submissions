class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = defaultdict(int)
        n = len(nums)
        for elem in nums:
            dict1[elem]+=1
            if dict1[elem]>n//2:
                return elem
        