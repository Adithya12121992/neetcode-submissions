class RandomizedSet:

    def __init__(self):
        self.dict1 = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.dict1:
            return False
        self.dict1[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict1:
            return False
        val_idx = self.dict1[val]
        last = self.values[-1]
        last_idx = self.dict1[last]
        self.values[val_idx] = last
        self.dict1[last] = val_idx
        del self.dict1[val]
        self.values.pop()
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()