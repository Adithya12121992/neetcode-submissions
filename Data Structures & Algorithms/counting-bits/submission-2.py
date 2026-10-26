class Solution:
    def countBits(self, n: int) -> List[int]:
        def find_ones(number):
            res = 0 
            while number:
                number &= ( number -1)
                res+=1
            return res
        ret = []
        for i in range(n+1):
            ret.append(find_ones(i))
        return ret
        
        