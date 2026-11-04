class RandomizedSet:

    def __init__(self):
        self.dict1 = {}
        self.list1 = []

    def insert(self, val: int) -> bool:
        if val in self.dict1:
            return False
        idx = len(self.list1)
        self.list1.append(val)
        self.dict1[val] = idx
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict1 or not self.list1:
            return False
        last_elem     = self.list1[-1]
        print(last_elem)
        print(self.list1)
        print(self.dict1)
        last_elem_idx = self.dict1[last_elem]
        curr_elem_idx = self.dict1[val]
        self.list1[last_elem_idx], self.list1[curr_elem_idx] = self.list1[curr_elem_idx], self.list1[last_elem_idx]
        self.dict1[last_elem] = curr_elem_idx
        self.list1.pop()
        del self.dict1[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.list1)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()