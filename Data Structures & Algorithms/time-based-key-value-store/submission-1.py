class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # we need to find the same or the closest
        if key not in self.data:
            return ""

        nums = self.data[key]
        l = 0
        r = len(nums)-1
        res = ""
        while l<=r:
            pivot = (l+r)//2
            if nums[pivot][0] <= timestamp:
                res = nums[pivot][1]
                l = pivot+1
            else:
                r = pivot-1
        return res
