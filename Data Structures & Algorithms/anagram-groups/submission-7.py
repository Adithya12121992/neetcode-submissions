class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for str1 in strs:
            ord_list = [0]*26
            for elem in str1:
                ord_list[ord(elem)-ord('a')]+=1
            dict1[tuple(ord_list)].append(str1)
        return list(dict1.values())