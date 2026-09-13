class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""
        need = defaultdict(int)
        want = defaultdict(int)
        res_len = math.inf
        result = (0,0)
        for elem in t:
            need[elem]+=1
        need_cnt = len(need)
        want_cnt = 0
        l = 0
        for r_index, r in enumerate(s):
            if r in need:
                want[r]+=1
                if want[r] == need[r]:
                    want_cnt+=1
                    while want_cnt == need_cnt:
                        if r_index-l+1 < res_len:
                            res_len = r_index-l+1
                            result = (l, r_index+1)
                        if s[l] in need:
                            want[s[l]]-=1
                            if want[s[l]] < need[s[l]]:
                                want_cnt-=1
                        l+=1
            else:
                continue
        return s[result[0]:result[1]] if res_len!=math.inf else ""
        
