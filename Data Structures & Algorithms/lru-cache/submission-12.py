class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.dict1 = {}
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left

    
    def _insert(self, key, val):
        head = self.left
        tail = self.right

        if key not in self.dict1:
            new_node = ListNode(key, val)
            self.dict1[key] = new_node
            prev_node = head.next
            head.next = new_node
            new_node.prev = head
            new_node.next = prev_node
            prev_node.prev = new_node

            if len(self.dict1) > self.size:
                self._remove()
        else:
            self.dict1[key].val = val
            new_node = self.dict1[key]
            prev_node = new_node.prev
            next_node = new_node.next
            
            if head.next == new_node:
                return 

            temp_node = head.next
            head.next = new_node
            new_node.prev = head
            new_node.next = temp_node
            temp_node.prev = new_node

            prev_node.next = next_node
            next_node.prev = prev_node
    
    def _remove(self):
        head = self.left
        tail = self.right

        if tail.prev and tail.prev.prev:
            del self.dict1[tail.prev.key]
            prev_node = tail.prev.prev
            prev_node.next = tail
            tail.prev = prev_node
        
        

    def get(self, key: int) -> int:
        if key not in self.dict1:
            return -1
        else:
            val = self.dict1[key].val
            self._insert(key, val)
            return val

    def put(self, key: int, value: int) -> None:
        self._insert(key, value)
        
