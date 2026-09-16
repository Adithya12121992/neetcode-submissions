class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        setl = defaultdict(int)
        setr = defaultdict(int)
        for l,r in trust:
            setl[l] +=1
            setr[r] +=1
        for i in range(1, n+1):
            if setl[i] == 0 and setr[i] == n-1:
                return i
        return -1