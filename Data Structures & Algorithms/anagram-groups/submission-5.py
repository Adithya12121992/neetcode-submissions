class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for elem in strs:
            can_val = [0]*26
            for i in range(len(elem)):
                can_val[ord('a')-ord(elem[i])]+=1
            dict1[tuple(can_val)].append(elem)
        return list(dict1.values())
