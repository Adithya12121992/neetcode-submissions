class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict1 = defaultdict(int)
        for elem in arr:
            dict1[elem]+=1
        result = []
        for elem in arr:
            if dict1[elem] == 1:
                result.append(elem)
        if len(result)<k:
            return ""
        else:
            return result[k-1]