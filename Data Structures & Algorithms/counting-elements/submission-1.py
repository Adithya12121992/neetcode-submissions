class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0
        set1 = set(arr)
        for elem in arr:
            if elem+1 in set1:
                res+=1
        return res
