class MedianFinder:

    def __init__(self):
        self.first_heap = []
        # the first half is always a max heap
        self.second_heap = []
        # the second half is always a min heap


    def addNum(self, num: int) -> None:
        # use heapq's peek
        if not self.first_heap and not self.second_heap:
            # first heap is max heap , so we multiply by -1 and make all min the max and max , the min elements
            heapq.heappush(self.first_heap, -1*num)
        else:
            if num <= (-1*self.first_heap[0]):
                heapq.heappush(self.first_heap, -1*num)
            else:
                heapq.heappush(self.second_heap, num)
        # balancing the 2 queues
        while abs(len(self.first_heap)-len(self.second_heap)) >1:
            if len(self.first_heap) > len(self.second_heap):
                #self.first_heap
                popped_elem = -1*heapq.heappop(self.first_heap)
                heapq.heappush(self.second_heap, popped_elem)
            else:
                #self.second_heap
                popped_elem = heapq.heappop(self.second_heap)
                heapq.heappush(self.first_heap, -1*popped_elem)            


    def findMedian(self) -> float:
        if len(self.first_heap) > len(self.second_heap):
            return -1*self.first_heap[0]
        elif len(self.first_heap) < len(self.second_heap):
            return self.second_heap[0]
        else:
            midl = -1*self.first_heap[0]
            midr = self.second_heap[0]
            return (midl+midr)/2