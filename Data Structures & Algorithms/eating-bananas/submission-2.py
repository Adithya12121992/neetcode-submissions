class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        l, r = 1, piles[-1]
        res = r

        while l<=r:
            mid = (l+r)//2
            time = 0
            for pile in piles:
                time+=math.ceil(pile/mid)
            if time<=h:
                res = mid
                r = mid-1
            else:
                l=mid+1
        return res