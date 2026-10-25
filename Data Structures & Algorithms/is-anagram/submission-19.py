class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1 = [0]*26
        for elem in s:
            dict1[(ord(elem)-ord('a'))]+=1
        for elem in t:
            dict1[(ord(elem)-ord('a'))]-=1
        return all(x==0 for x in dict1)