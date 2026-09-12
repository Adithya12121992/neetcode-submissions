class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''dicts = defaultdict(int)
        dictt = defaultdict(int)
        for elem in s:
            dicts[elem]+=1
        for elem in t:
            dictt[elem]+=1
        return dicts == dictt'''
        dict1 = [0]*26
        dict2 = [0]*26
        for elem in s:
            dict1[ord(elem)-ord('a')] +=1
        for elem in t:
            if dict1[ord(elem)-ord('a')] == 0:
                return False
            dict1[ord(elem)-ord('a')] -=1
        for elem in dict1:
            if elem >0:
                return False
        return True
