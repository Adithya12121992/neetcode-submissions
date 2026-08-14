class MedianFinder:

    def __init__(self):
        self.small = [] # holds the smaller half of the values in this array 
        self.large = [] # holds the  larger half of the values in this array

    def addNum(self, num: int) -> None:
        if self.large:
            if self.large[0] < num:
                heapq.heappush(self.large, num)
            else:
                heapq.heappush(self.small, -1 * num)
        else:
            heapq.heappush(self.large, num)
        while abs(len(self.small) - len(self.large)) > 1:
            if len(self.small) > len(self.large):
                heapq.heappush(self.large, -1 * heapq.heappop(self.small))
            else:
                heapq.heappush(self.small, -1 * heapq.heappop(self.large))
        
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            val1 = -1 * self.small[0]
            val2 = self.large[0]
            return (val1+val2)/2.0
        elif len(self.small) > len(self.large):
            return -1 * self.small[0]
        else:
            return self.large[0]