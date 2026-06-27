class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Adithya Solution
        chars = [0]*26
        for char in s:
            idx = ord(char)-ord('a')
            chars[idx]+=1
        for char in t:
            idx = ord(char)-ord('a')
            chars[idx]-=1
        if any(chars):
            return False
        return True
        