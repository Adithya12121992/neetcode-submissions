class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0]*len(arr)
        j=len(arr)-1
        max_val = -1
        for i in range(len(arr)-1, -1, -1):
            res[i] = max_val
            max_val = max(arr[i], max_val)
        return res
