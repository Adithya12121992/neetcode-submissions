class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for str1 in strs:
            flattened_string = [0]*26
            for elem in str1:
                flattened_string[ord(elem)-ord('a')]+=1
            grouped[tuple(flattened_string)].append(str1)
        return list(grouped.values())