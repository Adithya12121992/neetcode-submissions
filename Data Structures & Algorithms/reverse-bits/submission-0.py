class Solution:
    def reverseBits(self, n: int) -> int:
        bin_number = f'{n:032b}'
        num = [int(c) for c in bin_number]
        res = 0
        for i in range(32):
            res+=num[31-i]*(2**(31-i))
        return res