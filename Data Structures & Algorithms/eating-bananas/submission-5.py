class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_val = math.inf
        while left<=right:
            mid = (left+right)//2
            val = self.find_number(mid, piles)
            if val <= h:
                right = mid-1
                min_val = min(min_val, mid)
            else:
                left = mid+1
        return min_val
    def find_number(self, k, piles):
        cnt = 0
        for each_pile in piles:
            cnt += math.ceil(each_pile/k)
        return cnt