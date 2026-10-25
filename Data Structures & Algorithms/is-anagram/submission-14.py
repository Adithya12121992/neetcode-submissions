class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = [0]*26
        for elem in s:
            dict1[(ord('a')-ord(elem))]+=1
        for elem in t:
            dict1[(ord('a')-ord(elem))]-=1
        for elem in dict1:
            if elem <0 or elem>0:
                return False
        return True