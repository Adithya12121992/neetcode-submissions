class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = defaultdict(int)
        for elem in nums:
            dict1[elem]+=1
            if dict1[elem]>len(nums)//2:
                return elem
        