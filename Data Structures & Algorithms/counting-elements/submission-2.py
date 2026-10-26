class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0
        set1 = set(arr)
        # very important to iterate over arr and not set 
        for elem in arr:
            if elem+1 in set1:
                res+=1
        return res
