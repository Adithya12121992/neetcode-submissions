class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0
        i , j = 0, len(heights)-1
        # this is a 2 pointer problem
        while i < j:
            most_water = max(most_water , min(heights[i], heights[j])*(j-i))
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return most_water
