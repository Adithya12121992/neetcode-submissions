class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = self.return_list(height, False)
        maxr = self.return_list(height, True)
        sum1 = 0
        for idx, num in enumerate(height):
            val = min(maxl[idx], maxr[idx])-num
            if val<=0:
                continue
            sum1+=val
        return sum1

    def return_list(self, height, reverse):
        if reverse:
            height = height[::-1]
        return_list = [0]
        max_val = height[0]
        for i in range(1, len(height)):
            return_list.append(max_val)
            max_val = max(max_val, height[i])
        if reverse:
            return return_list[::-1]
        return return_list
