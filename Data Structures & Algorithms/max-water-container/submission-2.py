class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return_val = 0
        i , j = 0, len(heights)-1
        while i <= j:
            pts = min(heights[i], heights[j]) * (j-i)
            return_val = max(return_val, pts)
            if heights[i] < heights[j]:
                i+=1
            elif heights[i] > heights[j]:
                j-=1
            else:
                i+=1
                j-=1
        return return_val