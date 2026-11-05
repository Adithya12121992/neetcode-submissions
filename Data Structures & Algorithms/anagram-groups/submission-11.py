class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for elem in strs:
            index = [0]*26
            for each_elem in elem:
                index[ord(each_elem)-ord('a')]+=1
            dict1[tuple(index)].append(elem)
        return list(dict1.values())