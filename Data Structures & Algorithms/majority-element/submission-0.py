class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = defaultdict(int)
        for elem in nums:
            dict1[elem]+=1
        for key, val in dict1.items():
            if val>len(nums)//2:
                return key
        