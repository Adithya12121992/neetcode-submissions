class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rolling_sum = 0
        dict1 = defaultdict(int)
        result = 0
        dict1[0] = 1
        for num in nums:
            rolling_sum+=num
            diff = rolling_sum - k
            if diff in dict1:
                result+=dict1[diff]
            dict1[rolling_sum]+=1
        return result