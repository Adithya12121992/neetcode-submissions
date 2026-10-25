class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = defaultdict(int)
        for elem in s:
            dict1[elem]+=1
        for elem in t:
            if elem not in dict1:
                return False
            if dict1[elem]!=1:
                dict1[elem]-=1
            else:
                del dict1[elem]
        return not len(dict1)