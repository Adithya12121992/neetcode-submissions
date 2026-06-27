class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "__EMPTY_LIST__"
        ret = []
        for elem in strs:
            if elem == "":
                ret.append('E')
                continue
            each_ret = []
            for i in range(len(elem)):
                each_ret.append(str(ord(elem[i])))
            ret.append(",".join(each_ret))
        return "#".join(ret)

    def decode(self, s: str) -> List[str]:
        if s == "__EMPTY_LIST__":
            return []
        strings = s.split('#')
        return_val = []
        for each_str in strings:
            if each_str == 'E':
                return_val.append("")
                continue
            chars = each_str.split(',')
            ret = ""
            for char1 in chars:
                ret+=chr(int(char1))
            return_val.append(ret)
        return return_val

