class Solution:
    def hammingWeight(self, n: int) -> int:
        number = 0
        while n!=0:
            n, r = divmod(n, 2)
            number+=r
        return number