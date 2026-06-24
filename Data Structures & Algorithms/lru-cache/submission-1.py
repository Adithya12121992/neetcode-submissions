class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            # first , put the node at the end 
            node_to_move = self.cache[key]
            self.remove(node_to_move)
            self.insert(node_to_move)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache) > self.capacity:
                lru = self.left.next
                del self.cache[lru.key]
                self.remove(lru)

    def remove(self, node):
        prevN = node.prev
        nextN = node.next
        prevN.next = nextN
        nextN.prev = prevN
    
    def insert(self, node):
        prevN = self.right.prev
        nextN = self.right
        prevN.next = node
        node.prev = prevN
        node.next = nextN
        nextN.prev = node