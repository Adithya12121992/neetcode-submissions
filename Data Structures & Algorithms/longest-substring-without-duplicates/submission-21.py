class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()
        dict1 = set()
        max_val = 0
        for idx, elem in enumerate(s):
            if elem not in dict1:
                dict1.add(elem)
                queue.append(elem)
            else:
                max_val = max(max_val, len(queue))
                while queue and queue[0]!=elem:
                    elem1 = queue.popleft()
                    dict1.remove(elem1)
                if queue:
                    elem1 = queue.popleft()
                    dict1.remove(elem1)
                queue.append(elem)
                dict1.add(elem)
        max_val = max(max_val, len(queue))
        return max_val
