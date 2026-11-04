class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            interim = numbers[i]+numbers[j]
            if interim == target:
                return [i+1, j+1]
            elif interim > target:
                j-=1
            else:
                i+=1
        