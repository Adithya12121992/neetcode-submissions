class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for elem in strs:
            index = [0]*26
            for char in elem:
                index[ord(char)-ord('a')]+=1
            result[tuple(index)].append(elem)
        return list((result.values()))