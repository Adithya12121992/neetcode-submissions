class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capcaity = capacity
        self.dict1 = {}
        self.left = ListNode(None, None)
        self.right = ListNode(None, None)
        self.left.next = self.right
        self.right.prev = self.left
        
    def _insert(self, node):
        # insert alwasy to the left 
        next_node = self.left.next
        node.prev = self.left
        self.left.next = node
        node.next = next_node
        next_node.prev = node
        self.dict1[node.key] = node

    
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.dict1[node.key]


    def get(self, key: int) -> int:
        if key not in self.dict1:
            return -1
        node = self.dict1[key]
        self._remove(node)
        self._insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict1:
            node = self.dict1[key]
            node.val = value
            self._remove(node)
            self._insert(node)
        else:
            node = ListNode(key, value)
            self._insert(node)
            if len(self.dict1)>self.capcaity:
                self._remove(self.right.prev)
    

        
